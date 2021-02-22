#!/usr/bin/env python
from wtforms import Form, SubmitField


class DispenserForm(Form):

    save = SubmitField("save")
    cancel = SubmitField("cancel")


form = DispenserForm()
