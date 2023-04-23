from pydantic import BaseModel
from typing import Optional, List
from model.questionModel import AnswerType

class CreateAndUpdateQuestion(BaseModel):
    body : str
    maxMarks : int
    answerType : AnswerType
    answerId : int

class Question(CreateAndUpdateQuestion):
    id : int

    class Config:
        orm_mode = True

class PaginatedQuestion(BaseModel):
    limit: int
    offset: int
    data: List[Question]
 