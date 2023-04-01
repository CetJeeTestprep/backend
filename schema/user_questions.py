from datetime import datetime
import string
from pydantic import BaseModel

class UserQuestionsModel(BaseModel):
    id: str
    userId: str
    questionId: str
    questionPaperIds: list
    attempts: int
    leastTimeTaken: datetime.time
    mostTimeTaken: datetime.time

    def toJson(self):
        return {
            "id": self.id,
            "user_id": self.userId,
            "question_id": self.questionId,
            "question_paper_ids": self.questionPaperIds,
            "attempts": self.attempts,
            "least_time_taken": self.leastTimeTaken,
            "most_time_taken": self.mostTimeTaken
        }