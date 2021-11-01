from website import db

class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    question = db.Column(db.String(length=100), nullable=False, unique=True)


class Categories(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=100), nullable=False, unique=True)


class Answers(db.Model):
    __tablename__ = "answers"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=100), nullable=False, unique=True)


class Points(db.Model):
    __tablename__ = "points"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    question_id = db.ForeignKey('questions.id')
    category_id = db.ForeignKey('categories.id')
    answer_id = db.ForeignKey('answers.id')
    amount = db.Column(db.String(length=2))

