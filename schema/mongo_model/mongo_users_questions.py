from datetime import datetime
import string
from flask_mongoengine import Document, BaseField

class MongoUserQuestionsModel(Document):
    id: str = BaseField(db_field='id', primary_key=True)
    userId: str = BaseField(db_field='user_id', required=True)
    questionId: str = BaseField(db_field='question_id', required=True)
    questionPaperIds: list = BaseField(db_field='question_paper_ids_list')
    attempts: int = BaseField(db_field='attempts')
    leastTimeTaken: int = BaseField(db_field='least_time_taken')
    mostTimeTaken: int = BaseField(db_field='most_time_taken')
    correctAttempts: int = BaseField(db_field='correct_attempts')
    incorrectAttempts: int = BaseField(db_field='incorrect_attempts')

    meta = {
        'collection': 'user_questions'
    }