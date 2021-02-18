from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmiitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models.Users import Users

class RegistrationForm(FlaskForm):
    # username = StringField('Username',
    #                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create account')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
