import os
from flask import Flask, jsonify, render_template, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from .filters import datetimeformat, file_type, file_name
from datetime import timedelta


#passwd = os.environ.get('DB_passwd')
passwd="admin123!$"

POSTGRES_ADDRESS = "product-analytics-db-instance.cupv3jj2ht0z.us-west-2.rds.amazonaws.com"
POSTGRES_PORT = 5432
POSTGRES_USERNAME = "team9"
POSTGRES_PASSWORD = passwd
POSTGRES_DBNAME = "postgres"

postgres_str = 'postgresql+psycopg2://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(
    username=POSTGRES_USERNAME, 
    password=POSTGRES_PASSWORD, 
    ipaddress=POSTGRES_ADDRESS, 
    port=POSTGRES_PORT, 
    dbname=POSTGRES_DBNAME
)

app = Flask(__name__)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)
dropzone = Dropzone(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/shulun.chen/Documents/school_project/MSDS-603/back_end/project/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_str
app.config['SECRET_KEY'] = '1234567890'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
# app.config['WTF_CSRF_ENABLED'] = False
app.config['WTF_CSRF_SECRET_KEY'] = '1234567890'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SERVER_NAME'] = 'local.dev:5000'

app.config.from_pyfile("upload_to_s3/config.py")
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type
app.jinja_env.filters['file_name'] = file_name

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
# app.config['DROPZONE_REDIRECT_VIEW'] = 'users.results'

# Upload settings
# app.config['UPLOADED_PHOTOS_DEST'] = app.config['S3_LOCATION']
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"


from .models import User, Poll

@login_manager.user_loader
def load_user(uuid):
    return User.query.filter(User.uuid == uuid).first()


####################
#### blueprints ####
####################


from project.users.views import users_blueprint
from project.poll.views import poll_blueprint
from project.models import ValidationError


app.register_blueprint(users_blueprint)
app.register_blueprint(poll_blueprint)


# Error handling
@app.errorhandler(ValidationError)
def bad_request(e):
    response = jsonify({'status':400, 'error': 'bad request',
                        'message': e.args[0]})
    response.status_code = 400
    return response


@app.errorhandler(400)
def page_not_found(e):
    return make_response(jsonify({'error': 'Not found'}), 400)


@app.errorhandler(401)
def unauthorized(e):
    return redirect(url_for('users.login'))


@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('users.login'))


@app.errorhandler(403)
def forbidden(e):
    return redirect(url_for('/'))


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404


# @app.errorhandler(403)
# def page_not_found(e):
#     return render_template('403.html'), 403


if __name__ == "__main__":
    db.create_all()
