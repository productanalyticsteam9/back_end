from flask import render_template, flash, redirect, url_for, session, logging, request, Blueprint
from flask_login import login_user, current_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from uuid import uuid4

from .. import app, db
from ..models import User, Poll
from .forms import RegisterForm, LoginForm, UploadForm, PollForm
from ..upload_to_s3.helper import upload_file_to_s3
from ..resources import get_bucket, get_bucket_list
from werkzeug.utils import secure_filename 


poll_blueprint = Blueprint('poll', __name__)


@poll_blueprint.route("/poll")
def submit_poll():
    return render_template("submit_poll.html")


# @poll_blueprint.route("/user_home", methods=["GET", "POST"])
# @login_required
# def home():
#     return render_template("index_old.html")


# @users_blueprint.route("/login", methods=["GET", "POST"])
# def login():
#     session.permanent = True
#     form = LoginForm(request.form)
#     if request.method == "POST":
#         if form.validate_on_submit():
#             uname = request.form["username"]
#             passw = request.form["password"]

#             user = User.query.filter_by(username=uname).first()
#             if user is not None and user.is_correct_password(passw):
#                 user.authenticated = session.permanent
#                 user.last_login = user.current_login
#                 user.current_login = datetime.now()
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user)
#                 flash("Thanks for logging in, {}!".format(current_user.username), 'success')
#                 return redirect(url_for("users.home"))
#             else:
#                 flash("ERROR! Incorrect login credentials.", 'error')
#     return render_template("login.html", form=form)


# @users_blueprint.route("/register", methods=["GET", "POST"])
# def register():
#     form = RegisterForm(request.form)
#     if request.method == "POST":
#         if form.validate_on_submit():
#             try:
#                 uname = form.username.data
#                 mail = form.email.data
#                 passw = form.password.data
#                 age = form.age.data
#                 gender = form.gender.data
#                 city = form.city.data
#                 country_code = form.country.data
#                 browser = request.user_agent.browser

#                 # check_uname = User.query.filter_by(username=uname).first()
#                 user_count = User.query.filter_by(username=uname).count() + \
#                              User.query.filter_by(email=mail).count()
#                 # if check_uname is not None:
#                 if user_count > 0:
#                     flash("Sorry, username ({}) or email ({}) already exists.".format(uname, mail), 'error')
#                 else:
#                     register = User(username=uname, email=mail, plain_password=passw)
#                     register.uuid = str(uuid4())
#                     register.age = age
#                     register.gender = gender
#                     register.city = city
#                     register.country_code = country_code
#                     register.browser = browser
#                     register.authenticated = False
#                     db.session.add(register)
#                     db.session.commit()
#                     flash("Thank you for registering! Have a lovely day!", 'success')
#                     return redirect(url_for("users.login"))
#             except Exception as e:
#                 db.session.rollback()
#                 flash(e, 'error')
#         else:
#             flash("Sorry, the information you have entered does not conform to our standards, please reset them.", 'info')
#     return render_template("register.html", form=form)


# @users_blueprint.route("/logout")
# @login_required
# def logout():
#     user = current_user
#     user.authenticated = False
#     db.session.add(user)
#     db.session.commit()
#     logout_user()
#     flash("Goodbye and look forward to seeing you next time!", 'success')
#     return redirect(url_for("users.login"))


# @users_blueprint.route("/upload", methods=["GET", "POST"])
# @login_required
# def upload():
#     # if 'user_file' not in request.files:
#     #     return "Please select a file to upload."
    
#     # user = current_user
#     # form = UploadForm()
#     # if request.method == 'POST':
#     #     if form.validate_on_submit():
#     #         return_file = form.upload.data
#     #         if return_file:
#     #             return_file.filename = secure_filename(return_file.filename)
#     #             output = upload_file_to_s3(return_file, app.config['S3_BUCKET'], folder=user.uuid)
#     #             session['image_url'] = output
#     #             # return output, 200
#     #             return redirect(url_for('users.images'))
#     #         else:
#     #             return redirect(url_for("users.upload"))
#     #     else:
#     #         flash("Sorry, your file type is not allowed.", 'info')
#     # return render_template('upload.html', form=form)

#     user = current_user
#     if "file_urls" not in session:
#         session['file_urls'] = []
#     file_urls = session['file_urls']
#     print('hello')
#     print(request.method)
#     print(request.files, len(request.files))

#     if request.method == 'POST':
#         print('haha')
#         file_obj = request.files
#         for f in file_obj:
#             return_file = request.files.get(f)
#             url = upload_file_to_s3(return_file, app.config['S3_BUCKET'], folder=user.uuid)
#             print(url)
#             file_urls.append(url)

#         session['file_urls'] = file_urls
#         return "uploading..."
#     return render_template('dropzone.html')


# @users_blueprint.route("/results")
# @login_required
# def results():
    
#     # redirect to home if no images to display
#     if "file_urls" not in session or session['file_urls'] == []:
#         return redirect(url_for('users.upload'))
        
#     # set the file_urls and remove the session variable
#     file_urls = session['file_urls']
#     session.pop('file_urls', None)
    
#     return render_template('results.html', file_urls=file_urls)


# @users_blueprint.route("/images")
# @login_required
# def images():
#     url = session['image_url']
#     return render_template('images.html', url=url)


# @users_blueprint.route("/files")
# @login_required
# def files():
#     my_bucket = get_bucket()
#     summaries = my_bucket.objects.all()
#     return render_template('files.html', my_bucket=my_bucket, files=summaries)