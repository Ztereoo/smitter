from myapp import db
from datetime import datetime

class Posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(60),nullable=False)
    content=db.Column(db.Text,nullable=False)
    postdate=db.Column(db.DateTime, default=datetime.utcnow)
