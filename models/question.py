import string
from pydantic import BaseModel
class QuestionModel(BaseModel):
    id: str
    topic: str
    subtopic: str
    optionA: str
    optionB: str
    optionC: str
    optionD: str
    correctAns: str
    difficultyLevel: int