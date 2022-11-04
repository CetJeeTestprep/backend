import string
from pydantic import BaseModel
class UserModel(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    password: str
    
    #Student/Teacher
    userType: str

    #keys - qpId, score, attempts
    attemptedQuestionPapers: dict

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