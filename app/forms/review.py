#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Our first flask form"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    id = StringField("ID:", validators=[DataRequired()])
    review = StringField("Review:", validators=[DataRequired()])
    author = StringField("Author:", validators=[DataRequired()])
    