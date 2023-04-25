from pydantic import BaseModel
from typing import List
from model.questionModel import AnswerType

class CreateAndUpdateStudentTestMap(BaseModel):
    userEmail : str
    testId : int

class StudentTestMap(CreateAndUpdateStudentTestMap):
    id : int

    class Config:
        orm_mode = True

class PaginatedStudentTestMap(BaseModel):
    limit: int
    offset: int
    data: List[StudentTestMap]