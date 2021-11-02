from website import app
from flask import render_template, redirect, request
from .database import Database

question_answers = []


@app.route('/', methods=['GET'])
def home_page():
    question_answers.clear()
    return render_template("index.html")


@app.route('/question/<question_id>', methods=['GET'])
def question(question_id):
    database = Database(question_id, '')
    questions = database.get_current_question()
    answers = database.get_current_answers()

    return render_template("question.html", questions=questions, answers=answers, question_id=question_id)


@app.route('/question/<question_id>/process', methods=['POST'])
def process_question(question_id):
    question_answers.append(request.form['answer'])
    if int(question_id) + 1 < 3:
        print(question_answers)
        return redirect(f'/question/{int(question_id) + 1}')
    else:
        for index, value in enumerate(question_answers):
            database = Database(index + 1, value)
            answers = database.get_points()
            print(answers)
        # return redirect('/')
