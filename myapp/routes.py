from flask import Flask,render_template

from myapp import app

@app.route('/')
def index():
    return render_template('index.html')