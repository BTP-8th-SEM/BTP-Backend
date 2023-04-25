from pydantic import BaseModel
from typing import List
from model.questionModel import AnswerType

class CreateAndUpdateResponse(BaseModel):
    testId : int
    optionsId : int
    maxMarks : int
    topic : str
    body : str
    answerType : AnswerType

class Response(CreateAndUpdateResponse):
    id : int

    class Config:
        orm_mode = True

class PaginatedResponse(BaseModel):
    limit: int
    offset: int
    data: List[Response]
 