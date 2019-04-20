from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length, Optional


class PollForm(FlaskForm):
    poll_text = TextField('Poll Text', validators=[DataRequired()])
    user_tag = StringField('User Tag', validators=[Optional()])
