#!/usr/bin/env python
from wtforms import Form, TextField, DecimalField, HiddenField, validators, \
                          TextAreaField, SubmitField, SelectField
from bartendro.model import booze


class BoozeForm(Form):
    id = HiddenField("id", default=0)
    name = TextField("Name", [validators.Length(min=3, max=255)])
    brand = TextField("Brand") # Currently unused
    desc = TextAreaField("Description", [validators.Length(min=3, max=1024)])
    abv = DecimalField("ABV", [validators.NumberRange(0, 97)], default=0, places=0)
    type = SelectField("Type", [validators.NumberRange(0, len(booze.booze_types))], 
                                choices=booze.booze_types,
                                coerce=int)
    save = SubmitField("save")
    cancel = SubmitField("cancel")

form = BoozeForm()
