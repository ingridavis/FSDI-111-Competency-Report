#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Our first flask form"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    id = StringField("ID:", validators=[DataRequired()])
    first_name = StringField("First Name:", validators=[DataRequired()])
    last_name = StringField("Last Name:", validators=[DataRequired()])
    address = StringField("Address:", validators=[DataRequired()])
    billing_card = StringField("Billing Card:", validators=[DataRequired()])
    phone_number = StringField("Phone Number:", validators=[DataRequired()])
    submit = SubmitField("Submit")