from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(message='Please enter your first name')])
    last_name = StringField('Last name', validators=[DataRequired(message='Please enter your last name')])
    email = StringField('Email', validators=[DataRequired(message='Please enter your email'), Email(message='Please enter a valid email')])
    password = PasswordField('Password', validators=[DataRequired(message='Please enter your password'), EqualTo('confirm_password', message='Password must match')])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(message='Please enter your confirm password')])
    submit = SubmitField('Sign up')