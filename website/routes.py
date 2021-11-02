from website import app
from flask import render_template, redirect, url_for, flash
from .database import Database

@app.route('/', methods=['GET'])
def home_page():
    return render_template("index.html")

@app.route('/question/<question_id>', methods=['GET'])
def question(question_id):
    database = Database(question_id, '')
    questions = database.get_current_question()
    answers = database.get_current_answers()

    return render_template("question.html", questions=questions, answers=answers, question_id=question_id)

@app.route('/question/<question_id>/process', methods=['POST'])
def process_question(question_id):
    pass
