from flask import Flask,render_template,url_for,redirect,request,flash

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
        if title and content:
            new_post=Posts(title=title,content=content)
            db.session.add(new_post)
            db.session.commit()
            flash('Ваш пост добавлен')
            return redirect(url_for('posts'))
        else:
            flash('Заполните поля')
            return redirect(url_for('posts'))
    return render_template('create_post.html')

@app.route('/update/<int:post_id>', methods=['GET','POST'])
def update_post(post_id):
    post=Posts.query.get_or_404(post_id)

    if request.method=='POST':
        post.title= request.form.get('title')
        post.content= request.form.get('content')
        db.session.commit()
        flash('Пост успешно обновлен')
        return redirect(url_for('posts'))
    return render_template('update_post.html',post=post)

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post= Posts.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Запись удалена')
    return redirect(url_for('posts'))
