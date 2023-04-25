from pydantic import BaseModel
from typing import List, Optional
from model.questionModel import AnswerType

class CreateAndUpdateTest(BaseModel):
    name : str
    teacherId : int
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
    data: Optional[List[Test]] = None 