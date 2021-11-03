from website import app
from flask import render_template, redirect, request, url_for
from .database import Database
from .calculate import Calculate

question_answers = []


@app.route('/', methods=['GET'])
def home_page():
    question_answers.clear()
    return render_template("index.html")


@app.route('/question/<question_id>', methods=['GET'])
def question(question_id):
    database = Database()
    questions = database.get_current_question(question_id)
    answers = database.get_current_answers(question_id)

    return render_template("question.html", questions=questions, answers=answers, question_id=question_id)


@app.route('/question/<question_id>/process', methods=['POST'])
def process_question(question_id):
    database = Database()
    question_answers.append(request.form['answer'])
    if int(question_id) + 1 < 16:
        return redirect(f'/question/{int(question_id) + 1}')
    else:
        se = 0
        fict = 0
        bdam = 0
        iat = 0
        for index, value in enumerate(question_answers):
            answers = database.get_points(index + 1, value)
            for answer in answers:
                calculate = Calculate(answer[1], answer[2])
                if answer[0] == 'SE':
                    se = calculate.calculate_se(se)
                elif answer[0] == 'FICT':
                    fict = calculate.calculate_fict(fict)
                elif answer[0] == 'BDaM':
                    bdam = calculate.calculate_bdam(bdam)
                elif answer[0] == 'IAT':
                    iat = calculate.calculate_iat(iat)
        win = check_highest(se, bdam, fict, iat)
        return redirect(url_for('result', win=win))


@app.route('/result', methods=['GET'])
def result():
    database = Database()
    category = database.get_category_info(request.args['win'])

    return render_template('uitslag.html', category=category)


def check_highest(se, bdam, fict, iat):
    win = ''
    if se > bdam and se > fict and se > iat:
        win = 'SE'
    elif bdam > se and bdam > fict and bdam > iat:
        win = 'BDaM'
    elif fict > se and fict > bdam and fict > iat:
        win = 'FICT'
    elif iat > se and iat > bdam and iat > fict:
        win = 'IAT'

    return win
