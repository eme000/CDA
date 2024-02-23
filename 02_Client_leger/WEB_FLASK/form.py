from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=12, max=25, message="Username must be between 12 and 25 characters long."),
        Regexp('^[^<>]*$', message="Username cannot contain '<' or '>' characters.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=12, max=25, message="Password must be between 12 and 25 characters long."),
        Regexp('^[^<>]*$', message="Password cannot contain '<' or '>' characters.")
    ])
    submit = SubmitField('Sign up')
