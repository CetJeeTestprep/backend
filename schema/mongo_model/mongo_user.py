from flask_mongoengine import Document, BaseField

USER_TYPE_CHOICES = ['student', 'teacher']

class MongoUserModel(Document):
    id: str = BaseField(db_field='id', required=True, primary_key=True)
    name: str = BaseField(db_field='name', required=True)
    email: str = BaseField(db_field='email', required=True)
    phone: str = BaseField(db_field='phone')
    password: str = BaseField(db_field='password', required=True)
    userType: str = BaseField(db_field='user_type', choices=USER_TYPE_CHOICES)    
    attemptedQuestionPapers: dict = BaseField(db_field='attempted_question_paper')

    meta = {
        'collection': 'users'
    }