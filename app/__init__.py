#!/usr/bin/env python3
# -*- coding : utf8-*-

""" simple flask app"""



from flask import Flask # importing Flask class from flask module 
#path not properly set up, VSC not picking up virtual environment
from flask_bootstrap import Bootstrap 

app = Flask(__name__) # instantiating app variable with Flask class
Bootstrap(app)

app.config["SECRET_KEY"]="some string"


from app import routes 
# importing routes file from app module(folder)
