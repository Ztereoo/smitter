from flask_login import UserMixin
from myapp import db,manager
from datetime import datetime


class Posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(60),nullable=False)
    content=db.Column(db.Text,nullable=False)
    postdate=db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    login=db.Column(db.String(30),nullable=False,unique=True)
    password=db.Column(db.String(60),nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)