#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""UPDATE form"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UpdateForm(FlaskForm):
    id = StringField("ID:", validators=[DataRequired()])
    product_title = StringField("Product Name:", validators=[DataRequired()])
    brand_name = StringField("Product Brand Name:", validators=[DataRequired()])
    product_descrip = StringField("Product Description:", validators=[DataRequired()])
    product_price = StringField("Product Price:", validators=[DataRequired()])
    ship_price = StringField("Ship Price:", validators=[DataRequired()])
    sku = StringField("SKU Number:", validators=[DataRequired()])
    submit = SubmitField("Submit")
    