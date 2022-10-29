import string
from pydantic import BaseModel
class UserModel(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    password: str
    userType: str

    #keys - qpId, score, attempts
    attemptedQuestionPapers: dict