from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_toastr import Toastr


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='abrababra21{]!'
manager=LoginManager(app)
db=SQLAlchemy(app)
toastr = Toastr(app)

from myapp import models,routes

with app.app_context():

    db.create_all()

