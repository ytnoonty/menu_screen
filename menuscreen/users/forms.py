from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from menuscreen.models import User

# Register Form Class
class RegisterForm(FlaskForm):
    name = StringField('Name', [
        validators.Length(min=5, max=50),
        validators.DataRequired()
    ])
    venuename = StringField('Venue Name', [
        validators.Length(min=5, max=50),
        validators.DataRequired()
    ])
    username = StringField('Username', [
        validators.Length(min=5, max=25),
        validators.DataRequired()
    ])
    websiteURL = StringField('Website Address', [
        validators.Length(min=15, max=200)
    ])
    email = StringField('Email', [
        validators.Length(min=5, max=100),
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField('Password', [
        validators.Length(min=5, max=20),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password', [
        validators.DataRequired()
    ])
    submit = SubmitField('Sign Up')

    # WTF validation method to find if duplicate name
    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('Nameame is already in use, Please choose a different one.')
    # WTF validation method to find if duplicate venuename
    def validate_venuename(self, venuename):
        user = User.query.filter_by(venue_name=venuename.data).first()
        if user:
            raise ValidationError('Venuename is already in use, Please choose a different one.')
    # WTF validation method to find if duplicate username
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already in use, Please choose a different one.')
    # WTF validation method to find if duplicate email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already taken, Please choose a different one.')

# Login Form Class
class LoginForm(FlaskForm):
    username = StringField('Username',
        validators=[DataRequired()])
    password = PasswordField('Password',
        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# Register Form Class
class UpdateAccountForm(FlaskForm):
    name = StringField('Name', [
        validators.Length(min=5, max=50),
        validators.DataRequired()
    ])
    venuename = StringField('Venue Name', [
        validators.Length(min=5, max=50),
        validators.DataRequired()
    ])
    username = StringField('Username', [
        validators.Length(min=5, max=25),
        validators.DataRequired()
    ])
    email = StringField('Email', [
        validators.Length(min=5, max=100),
        validators.DataRequired(),
        validators.Email()
    ])
    picture = FileField('Update Profile Picture', validators=[
        FileAllowed(['jpg'], 'Images Only!')
    ])
    submit = SubmitField('Update')

    # WTF validation method to find if duplicate name
    def validate_name(self, name):
        if name.data != current_user.name:
            user = User.query.filter_by(name=name.data).first()
            if user:
                raise ValidationError('Name is already in use, Please choose a different one.')

    # WTF validation method to find if duplicate venuename
    def validate_venuename(self, venuename):
        if venuename.data != current_user.venue_name:
            user = User.query.filter_by(venue_name=venuename.data).first()
            if user:
                raise ValidationError('Venuename is already in use, Please choose a different one.')

    # WTF validation method to find if duplicate username
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already in use, Please choose a different one.')

    # WTF validation method to find if duplicate email
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is already taken, Please choose a different one.')


class RequestResetForm(FlaskForm):
    email = StringField('Email', [
        validators.Length(min=5, max=100),
        validators.DataRequired(),
        validators.Email()
    ])
    submit = SubmitField('Request Password Reset')
    # WTF validation method to find if duplicate email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', [
        validators.Length(min=5, max=20),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password', [
        validators.DataRequired()
    ])
    submit = SubmitField('Reset Password')
