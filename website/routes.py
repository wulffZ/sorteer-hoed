from website import app
from flask import render_template, redirect, url_for, flash
from website.models import Questions, Categories, Points, Answers
from website import db

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/question')
def question():
    return render_template("question.html")
