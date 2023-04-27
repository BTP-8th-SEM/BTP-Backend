from pydantic import BaseModel
from typing import List
from model.questionModel import AnswerType

class CreateAndUpdateResponse(BaseModel):
    questionId : int
    userEmail : str
    testId : int 
    body : str
    obtainedMarks : int

class Response(CreateAndUpdateResponse):
    id : int

    class Config:
        orm_mode = True

class PaginatedResponse(BaseModel):
    limit: int
    offset: int
    data: List[Response]
 