from flask_mongoengine import Document, BaseField

USER_TYPE_CHOICES = ['student', 'teacher']

class MongoUserModel(Document):
    id: str = BaseField(db_field='id', primary_key=True)
    name: str = BaseField(db_field='name')
    email: str = BaseField(db_field='email')
    phone: str = BaseField(db_field='phone')
    password: str = BaseField(db_field='password')
    userType: str = BaseField(db_field='user_type', choices=USER_TYPE_CHOICES)    
    attemptedQuestionPapers: str = BaseField(db_field='attempted_question_paper')
    confidence_score: float = BaseField(db_field='confidence_score')
    accuracy_score: float = BaseField(db_field='accuracy_score')
    strengths: str = BaseField(db_field='strengths')
    weaknesses: str = BaseField(db_field='weaknesses')

    meta = {
        'collection': 'users'
    }

