from pydantic import BaseModel
from typing import List

class CreateAndUpdateOLAPQuestions(BaseModel):
    questionId : int
    maxMarks : int
    highestMarks : int
    lowestMarks : int
    avgMarks : int
    topic : str

class OLAPQuestions(CreateAndUpdateOLAPQuestions):
    id : int

    class Config:
        orm_mode = True

class PaginatedOLAPQuestions(BaseModel):
    limit: int
    offset: int
    data: List[OLAPQuestions]