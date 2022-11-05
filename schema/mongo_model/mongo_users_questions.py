from datetime import datetime
import string
from flask_mongoengine import Document, BaseField

class MongoUserQuestionsModel(Document):
    id: str = BaseField(db_field='id', required=True, primary_key=True)
    userId: str = BaseField(db_field='user_id', required=True)
    questionId: str = BaseField(db_field='question_id', required=True)
    questionPaperIds: list = BaseField(db_field='question_paper_id')
    attempts: int = BaseField(db_field='attempts')
    leastTimeTaken: datetime.time = BaseField(db_field='least_time_taken')
    mostTimeTaken: datetime.time = BaseField(db_field='most_time_taken')

    meta = {
        'collections': 'user_questions'
    }