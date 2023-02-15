#registration.py
from flask_wtf import Form
from wtforms import String Field, PasswordField, SubmitField
from wtforms import validators, ValidationError
from wtforms.validators import InputRequired, Email




class Registration(Form):
    email = StringField("email", [validators.InputRequired ("please enter your email"), validators.Email('invalid email') IsUnique]))
    password = PasswordField('password',[validators.InputRequired ("please enter a password")])
    confirm password = PasswordField("confirm password". [validators.InputRequired ("password"), validators.EqualTo("password", "passwords must match")])

    submit =