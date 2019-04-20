from project import db
from project import bcrypt as bcrypt_app
import bcrypt
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy import Integer, String
from sqlalchemy.dialects import postgresql
from datetime import datetime


schema = 'appdata'

class User(db.Model):

    __tablename__ = schema+'.'+'user'

    uuid = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    p_password = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(3))
    city = db.Column(db.String(20))
    country_code = db.Column(db.String(3))
    browser = db.Column(db.String(10))
    is_developer = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    current_login = db.Column(db.DateTime)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, plain_password):
        self.username = username
        self.email = email
        self.password = plain_password
        self.authenticated = False
        self.created_on = datetime.now()
        self.current_login = datetime.now()
    
    @hybrid_property
    def password(self):
        return self.p_password

    @password.setter
    def password(self, plain_password):
        pwhash = bcrypt.hashpw(plain_password.encode('utf8'), bcrypt.gensalt())
        self.p_password = pwhash.decode('utf8')

    @hybrid_method
    def is_correct_password(self, plain_password):
        return bcrypt_app.check_password_hash(self.password, plain_password)

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.uuid

    def __repr__(self):
        return '<User {}>'.format(self.username)


class ValidationError(ValueError):
    pass


class Poll(db.Model):

    __tablename__ = schema+'.'+'poll'

    poll_text = db.Column(db.String(200), nullable=False)
    poll_uuid = db.Column(db.String(100), primary_key=True)
    uuid = db.Column(db.String(100), nullable=False)
    image_id = db.Column(postgresql.ARRAY(Integer), nullable=False)
    image_path = db.Column(postgresql.ARRAY(String), nullable=False)
    vote_cnt = db.Column(postgresql.ARRAY(Integer))
    post_date = db.Column(db.DateTime)
    user_tag = db.Column(db.String(80))
    model_tag = db.Column(db.String(80))    

    def __init__(self, poll_text, poll_uuid, uuid, image_id, image_path):
        self.poll_text = poll_text
        self.poll_uuid = poll_uuid
        self.uuid = uuid
        self.image_id = image_id
        self.image_path = image_path
        self.post_date = datetime.now()



        