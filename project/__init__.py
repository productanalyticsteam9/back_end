from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


passwd = os.environ.get('DB_passwd')

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
# csrf.init_app(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/shulun.chen/Documents/school_project/MSDS-603/back_end/project/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_str
app.config['SECRET_KEY'] = '1234567890'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SERVER_NAME'] = 'local.dev:5000'

app.config.from_pyfile("upload_to_s3/config.py")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"


from .models import User

@login_manager.user_loader
def load_user(uuid):
    return User.query.filter(User.uuid == uuid).first()


####################
#### blueprints ####
####################


from project.users.views import users_blueprint


app.register_blueprint(users_blueprint)
