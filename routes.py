from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render template('index.html')

@app.route
def about():
    return render_template('about.html')
