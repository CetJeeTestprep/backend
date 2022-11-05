import string
from pydantic import BaseModel
from flask_mongoengine import Document, BaseField

USER_TYPE_CHOICES = ['student', 'teacher']

class UserModel(BaseModel):


    id: str
    name: str
    email: str
    phone: str
    password: str
    
    #Student/Teacher
    userType: str = BaseField(db_field='user_type', choices=USER_TYPE_CHOICES)

    #keys - qpId, score, attempts
    attemptedQuestionPapers: dict = BaseField(db_field='attempted_question_paper')

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "user_type": self.userType,
            "attempted_question_papers": self.attemptedQuestionPapers
        }




# class User(db.Document):
#     id = db.StringField()
#     name = db.StringField()
#     email = db.StringField()
#     phone = db.StringField()
#     password = db.StringField()
#     userType = db.StringField()
#     #attemptedQuestionPapers = db.DictField()