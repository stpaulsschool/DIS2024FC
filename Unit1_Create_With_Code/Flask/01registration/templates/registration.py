#registration.py
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators, ValidationError
from wtforms.validators import InputRequired, Email, EqualTo
from testemail import IsUnique




class Registration(Form):
    email = StringField("email", [validators.InputRequired ("please enter your email"), validators.Email('invalid email'), IsUnique])
    password = PasswordField('password',[validators.InputRequired ("please enter a password")])
    confirm_password = PasswordField("confirm password", [validators.InputRequired ("password"), validators.EqualTo("password", "passwords must match")])

    submit = SubmitField("Submit")