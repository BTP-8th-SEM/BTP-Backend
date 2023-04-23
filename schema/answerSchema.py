from pydantic import BaseModel
from typing import List

class CreateAndUpdateAnswer(BaseModel):
    option1 : int
    option2 : int
    option3 : int
    option4 : int
    CorrectOption : int

class Answer(CreateAndUpdateAnswer):
    id : int

    class Config:
        orm_mode = True

class PaginatedAnswerInfo(BaseModel):
    limit: int
    offset: int
    data: List[Answer]
 