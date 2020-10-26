#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Our first flask form"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AdminForm(FlaskForm):
    password = StringField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")