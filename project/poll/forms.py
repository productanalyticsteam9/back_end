from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, IntegerField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange, Optional
import pycountry as pc

class PollForm(FlaskForm):
    poll_text = StringField('Poll Text', validators=[DataRequired(), Length(min=0, max=150)])