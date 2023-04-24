from pydantic import BaseModel
from typing import List
from model.questionModel import AnswerType

class CreateAndUpdateTest(BaseModel):
    name : str
    maxMarks : int
    passMarks : int
    testType : AnswerType
    startTime : str
    endTime : str

class Test(CreateAndUpdateTest):
    id : int
    sharableId : str

    class Config:
        orm_mode = True

class PaginatedTest(BaseModel):
    limit: int
    offset: int
    data: List[Test]