from website import db


class Database(object):
    def __init__(self, question_id, answer_id):
        self.connection = db.connection.cursor()
        self.question_id = question_id
        self.answer_id = answer_id

    def get_current_question(self):
        self.connection.execute(f"SELECT * "
                                f"FROM questions "
                                f"WHERE questions.id = {self.question_id}")

        question = self.connection.fetchall()
        return question

    def get_current_answers(self):
        self.connection.execute(
            f"SELECT answers.id, MAX(answers.answer) "
            f"FROM points "
            f"INNER JOIN answers ON answers.id = points.answer_id "
            f"WHERE points.question_id = {self.question_id} "
            f"GROUP BY answers.id")

        answers = self.connection.fetchall()
        return answers

    def get_points(self):
        self.connection.execute(
            f"SELECT * "
            f"FROM points "
            f"LEFT JOIN categories ON categories.id = points.category_id "
            f"WHERE points.answer_id = {self.answer_id} AND points.question_id = {self.question_id}")
        data = self.connection.fetchall()
        return data
