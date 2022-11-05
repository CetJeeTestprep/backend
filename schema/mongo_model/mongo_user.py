from flask_mongoengine import Document, BaseField

USER_TYPE_CHOICES = ['student', 'teacher']

class MongoUserModel(Document):
    id: str = BaseField(db_field='id', primary_key=True)
    name: str = BaseField(db_field='name')
    email: str = BaseField(db_field='email')
    phone: str = BaseField(db_field='phone')
    password: str = BaseField(db_field='password')
    userType: str = BaseField(db_field='user_type', choices=USER_TYPE_CHOICES)    
    attemptedQuestionPapers: dict = BaseField(db_field='attempted_question_paper')


    meta = {
        'collection': 'users'
    }

