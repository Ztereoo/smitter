from flask import render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user,login_required
from werkzeug.security import check_password_hash, generate_password_hash
from myapp import app, db
from .models import Posts, User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
@login_required
def posts():
    allposts = Posts.query.all()
    return render_template('posts.html', posts=allposts)


@app.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if title and content:
            new_post = Posts(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            flash('Ваш пост добавлен', 'success')
            return redirect(url_for('posts'))
        else:
            flash('Заполните поля', 'warning')
            return redirect(url_for('posts'))
    return render_template('create_post.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Posts.query.get_or_404(post_id)

    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        db.session.commit()
        flash('Пост успешно обновлен', 'success')
        return redirect(url_for('posts'))
    return render_template('update_post.html', post=post)


@app.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Запись удалена', 'info')
    return redirect(url_for('posts'))


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        if keyword:
            keyword = keyword.strip()
            results = Posts.query.filter(
                db.or_(
                    Posts.title.ilike(f'{keyword}'),
                    Posts.title.ilike(f'{keyword} %'),
                    Posts.title.ilike(f'% {keyword}'),
                    Posts.title.ilike(f'% {keyword} %'),

                    Posts.content.ilike(f'{keyword}'),
                    Posts.content.ilike(f'{keyword} %'),
                    Posts.content.ilike(f'% {keyword}'),
                    Posts.content.ilike(f'% {keyword} %')
                )
            ).all()
            return render_template('posts.html', posts=results, keyword=keyword)
        else:
            flash('Введите ключевое слово для поиска', 'warning')
            return redirect(url_for('posts'))
    return redirect(url_for('posts'))


@app.route('/login', methods=['POST', 'GET'])
def login_func():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('pass')

        if login and password:
            user = User.query.filter_by(login=login).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash('Login success', 'success')
                return redirect(url_for('posts'))
            else:
                flash('неправильнй пароль', 'warning')
                return render_template('login.html')
        else:
            flash('заполните все поля', 'warning')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    login = request.form.get('login')
    password = request.form.get('pass')
    password2 = request.form.get('confirm_pass')
    if request.method == 'POST':
        if not (login or password or password2):
            flash('Заполните все поля', 'warning')
        elif len(password) < 6:
            flash('Пароль должен быть не менее 6 символов','warning')
        elif password != password2:
            flash('пароли не совпадают', 'error')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()
            flash('Вы успешно зарегестрировались', 'success')
            return redirect(url_for('login_func'))

    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

@app.after_request
def redirect_to_signin(response):
    if response.status_code== 401:
        return redirect(url_for('login_func'))
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
