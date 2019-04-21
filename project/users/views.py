from flask import render_template, flash, redirect, url_for, session, logging, request, Blueprint, Response, send_file
from flask_login import login_user, current_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from uuid import uuid4

from .. import app, db
from ..models import User
from .forms import RegisterForm, LoginForm, UploadForm
from ..upload_to_s3.helper import upload_file_to_s3, generate_file_url
from ..upload_to_s3.config import S3_BUCKET
from ..resources import get_bucket, get_bucket_list, _get_s3_client
from werkzeug.utils import secure_filename 


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route("/")
def index():
    return render_template("index.html")


@users_blueprint.route("/user_home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("index_old.html")


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    session.permanent = True
    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            uname = request.form["username"]
            passw = request.form["password"]

            user = User.query.filter_by(username=uname).first()
            if user is not None and user.is_correct_password(passw):
                user.authenticated = session.permanent
                user.last_login = user.current_login
                user.current_login = datetime.now()
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash("Thanks for logging in, {}!".format(current_user.username), 'success')
                return redirect(url_for("users.home"))
            else:
                flash("ERROR! Incorrect login credentials.", 'error')
    return render_template("login.html", form=form)


@users_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                uname = form.username.data
                mail = form.email.data
                passw = form.password.data
                age = form.age.data
                gender = form.gender.data
                city = form.city.data
                country_code = form.country.data
                browser = request.user_agent.browser

                # check_uname = User.query.filter_by(username=uname).first()
                user_count = User.query.filter_by(username=uname).count() + \
                             User.query.filter_by(email=mail).count()
                # if check_uname is not None:
                if user_count > 0:
                    flash("Sorry, username ({}) or email ({}) already exists.".format(uname, mail), 'error')
                else:
                    register = User(username=uname, email=mail, plain_password=passw)
                    register.uuid = uuid4()
                    register.age = age
                    register.gender = gender
                    register.city = city
                    register.country_code = country_code
                    register.browser = browser
                    register.authenticated = False
                    db.session.add(register)
                    db.session.commit()
                    flash("Thank you for registering! Have a lovely day!", 'success')
                    return redirect(url_for("users.login"))
            except Exception as e:
                db.session.rollback()
                flash(e, 'error')
        else:
            flash("Sorry, the information you have entered does not conform to our standards, please reset them.", 'info')
    return render_template("register.html", form=form)


@users_blueprint.route("/logout")
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    session.clear()
    logout_user()
    flash("Goodbye and look forward to seeing you next time!", 'success')
    return redirect(url_for("users.login"))


@users_blueprint.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    user = current_user
    form = UploadForm()
    if "file_urls" not in session:
        session['file_urls'] = []
    file_urls = session['file_urls']
    poll_uuid = uuid4()
    if request.method == 'POST':
        if form.validate_on_submit() and request.files:
            for f in request.files.getlist('upload'):
                f.filename = secure_filename(f.filename)
                upload_file_to_s3(f, S3_BUCKET, poll=poll_uuid, folder=user.uuid)
                url = generate_file_url(f, S3_BUCKET, poll=poll_uuid, folder=user.uuid)
                file_urls.append(url)
            session['file_urls'] = file_urls
            session['poll_uuid'] = poll_uuid
            return redirect(url_for('poll.submit_poll'))

    return render_template('upload.html', form=form)


@users_blueprint.route("/download", methods=["GET"])
@login_required
def download():
    key = request.form['key']
    print(key)
    my_bucket = get_bucket()
    file_obj = my_bucket.Object(key).get()
    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )


@users_blueprint.route("/files", methods=['GET'])
@login_required
def files():
    user = current_user
    my_bucket = get_bucket()
    summaries = my_bucket.objects.filter(Prefix=user.uuid)
    get_last_modified = lambda obj: int(obj.last_modified.strftime('%s'))
    files = [obj for obj in sorted(summaries, key=get_last_modified, reverse=True)]
    return render_template('files.html', my_bucket=my_bucket, files=files)