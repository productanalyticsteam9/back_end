from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/shulun.chen/Documents/school_project/MSDS-603/back_end/project/database.db'
app.config['SECRET_KEY'] = '1234567890'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SERVER_NAME'] = 'local.dev:5000'
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
