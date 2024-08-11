from flask import Flask,render_template,url_for,redirect,request

from myapp import app,db
from .models import Posts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    allposts=Posts.query.all()
    return render_template('posts.html',posts=allposts)

@app.route('/create', methods=['POST','GET'])
def create_post():
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content']
        new_post=Posts(title=title,content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts'))
    return render_template('create_post.html')