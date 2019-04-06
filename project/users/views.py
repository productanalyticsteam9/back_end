from flask import render_template, flash, redirect, url_for, session, logging, request, Blueprint
from flask_login import login_user, current_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from uuid import uuid4

from .. import app, db
from ..models import User
from .forms import RegisterForm, LoginForm, UploadForm
from ..upload_to_s3.helper import upload_file_to_s3
from werkzeug.utils import secure_filename 


users_blueprint = Blueprint('users', __name__)

@users_blueprint.route("/")
def index():
    return render_template("index.html")


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            uname = request.form["username"]
            passw = request.form["password"]

            user = User.query.filter_by(username=uname).first()
            if user is not None and user.is_correct_password(passw):
                user.authenticated = True
                user.last_login = user.current_login
                user.current_login = datetime.now()
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash("Thanks for logging in, {}!".format(current_user.username), 'success')
                return redirect(url_for("users.index"))
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

                check_uname = User.query.filter_by(username=uname).first()
                if check_uname is not None:
                    flash("Sorry, username ({}) already exists.".format(uname), 'error')
                else:
                    register = User(username=uname, email=mail, plain_password=passw)
                    register.uuid = str(uuid4())
                    register.age = age
                    register.gender = gender
                    register.city = city
                    register.country_code = country_code
                    register.browser = browser
                    register.authenticated = True
                    db.session.add(register)
                    db.session.commit()
                    flash("Thank you for registering! Have a lovely day!", 'success')
                    return redirect(url_for("users.login"))
            except Exception as e:
                db.session.rollback()
                flash(e, 'error')
        else:
            flash("Sorry, your credentials do not conform to our standards, please reset them.", 'info')
    return render_template("register.html", form=form)


@users_blueprint.route("/logout")
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash("Goodbye and look forward to see you next time!", 'success')
    return redirect(url_for("users.login"))


@users_blueprint.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    # if 'user_file' not in request.files:
    #     return "Please select a file to upload."
    
    user = current_user
    form = UploadForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return_file = form.upload.data
            if return_file:
                return_file.filename = secure_filename(return_file.filename)
                output = upload_file_to_s3(return_file, app.config['S3_BUCKET'], folder=user.uuid)
                return output, 200
            else:
                return redirect(url_for("users.upload"))
        else:
            flash("Sorry, your file type is not allowed.", 'info')
    return render_template('upload.html', form=form)
