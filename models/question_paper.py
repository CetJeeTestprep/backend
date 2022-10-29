from datetime import datetime
import string
from pydantic import BaseModel

class QuestionPaperModel(BaseModel):
    id: str
    date: datetime
    difficulty: float
    
    #cet/jee
    exam: str
    
    #chapter/subject/overall
    type: str

    maxAttempts: int
    marksPerQuestion: int
    totalMarks: int
    questions: list