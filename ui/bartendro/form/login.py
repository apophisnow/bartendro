#!/usr/bin/env python
from wtforms import Form, TextField, PasswordField, SubmitField, validators


class LoginForm(Form):
    user = TextField("Name", [validators.Length(min=3, max=255)])
    password = PasswordField("Password", [validators.Length(min=3, max=255)])

    login = SubmitField("login")


form = LoginForm()
