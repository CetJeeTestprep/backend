import datetime
from flask_mongoengine import Document, BaseField


class MongoQuestionPaperModel(Document):

    id: str = BaseField(db_field='id', primary_key=True)
    date: datetime = BaseField(db_field='date')
    difficulty: float = BaseField(db_field='difficutlty')
    
    #cet/jee
    exam: str = BaseField(db_field='exam')
    
    #chapter/subject/overall
    type: str = BaseField(db_field='type')

    maxAttempts: int = BaseField(db_field='max_attempt')
    marksPerQuestion: int = BaseField(db_field='marks_per_question')
    totalMarks: int = BaseField(db_field='total_marks')
    questions: list = BaseField(db_field='questions')
    duration: datetime.time = BaseField(db_field='duration')
    meta = {
        'collection': 'question_papers'
    }