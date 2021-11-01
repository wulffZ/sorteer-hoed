from website import app
from flask import render_template, redirect, url_for, flash
from website.models import Questions, Categories, Points, Answers
from website import db

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/hoi')
def hoi():
    items = Answers.query.all()
    return render_template('hoi.html', items=items)
