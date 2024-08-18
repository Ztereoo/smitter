from flask import Flask,render_template,url_for,redirect,request,flash
from flask_login import login_user
from werkzeug.security import check_password_hash,generate_password_hash
from myapp import app,db
from .models import Posts,User

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

@app.route('/login', methods=['POST','GET'])
def login_func():
    if request.method=='POST':
        login = request.form.get('login')
        password = request.form.get('pass')

        if login and password:
            user = User.query.filter_by(login=login).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('posts'))
            else:
                flash('неправильнй пароль')
                return render_template('login.html')
        else:
            flash('заполните все поля')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/register',methods=['POST','GET'])
def register():
    login= request.form.get('login')
    password= request.form.get('pass')
    password2=request.form.get('confirm_pass')
    if request.method=='POST':
        if not (login or password or password2):
            flash('Заполните все поля')
        elif password != password2:
            flash('пароли не совпадают')
        else:
            hash_pwd=generate_password_hash(password)
            new_user= User(login=login,password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()
            flash('Вы успешно зарегестрировались')
            return redirect(url_for('login_func'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))