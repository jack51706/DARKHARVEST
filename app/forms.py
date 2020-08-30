# Inherit from flask_wtf
from flask_wtf import FlaskForm

# Import field classes
from wtforms import StringField, PasswordField, BooleanField, SubmitField

# Import validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

# Import user database table
from app.models import User

# Class defining form using for initial login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class ShellForm(FlaskForm):
    command = StringField('Command:')
    execute = SubmitField('Execute')
    kill = SubmitField('Kill')
