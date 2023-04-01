import datetime
from flask_mongoengine import Document, BaseField

class MongoResultsModel(Document):
    id: str = BaseField(db_field='id', primary_key=True)
    question_paper_id: str = BaseField(db_field='question_paper_id')
    user_id: str = BaseField(db_field='user_id')
    final_score: int = BaseField(db_field='final_score')
    total_possible_score: int = BaseField(db_field='total_possible_score')    
    question_wise_results: list = BaseField(db_field='question_wise_results')
    time_completed: datetime = BaseField(db_field='time_completed')
    total_time_taken: int = BaseField(db_field='total_time_taken')

    meta = {
        'collection': 'results'
    }

