from pydantic import BaseModel
from typing import List
from model.questionModel import AnswerType

class CreateAndUpdateQuestion(BaseModel):
    testId : int
    optionsId : int
    maxMarks : int
    topic : str
    body : str
    answerType : AnswerType

class Question(CreateAndUpdateQuestion):
    id : int

    class Config:
        orm_mode = True

class PaginatedQuestion(BaseModel):
    limit: int
    offset: int
    data: List[Question]
 