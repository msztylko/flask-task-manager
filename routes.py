from app import app, db
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('about.html', form=form)
