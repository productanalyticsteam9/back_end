from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange, Optional
import pycountry as pc


country_code = [c.alpha_2.lower() for c in pc.countries]
country = [c.name for c in pc.countries]
countries = [(co, c) for co, c in zip(country_code, country)]
countries = sorted(countries, key=lambda tup: tup[1])

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=40)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=150)])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    city = TextAreaField('City', validators=[DataRequired(), Length(max=20)])
    country = SelectField('Country', choices=countries, validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Password must match")])


class LoginForm(FlaskForm):
    # email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=40)])
    password = PasswordField('Password', validators=[DataRequired()])


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])


class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])