from website import db


class Database(object):
    def __init__(self):
        self.connection = db.connection.cursor()

    def get_current_question(self, question_id):
        self.connection.execute(f"SELECT * "
                                f"FROM questions "
                                f"WHERE questions.id = {question_id}")

        question = self.connection.fetchall()
        return question

    def get_current_answers(self, question_id):
        self.connection.execute(
            f"SELECT answers.id, MAX(answers.answer) "
            f"FROM points "
            f"INNER JOIN answers ON answers.id = points.answer_id "
            f"WHERE points.question_id = {question_id} "
            f"GROUP BY answers.id")

        answers = self.connection.fetchall()
        return answers

    def get_points(self, question_id, answer_id):
        self.connection.execute(
            f"SELECT categories.name, points.operator, points.amount "
            f"FROM points "
            f"LEFT JOIN categories ON categories.id = points.category_id "
            f"WHERE points.answer_id = {answer_id} AND points.question_id = {question_id}")
        data = self.connection.fetchall()
        return data

    def get_category_info(self, category_name):
        self.connection.execute(
            f"SELECT * "
            f"FROM categories "
            f"WHERE categories.name = '{category_name}'"
        )

        category = self.connection.fetchone()
        return category
