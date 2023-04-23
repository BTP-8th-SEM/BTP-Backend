from pydantic import BaseModel
from typing import List

class CreateAndUpdateOptions(BaseModel):
    option1 : int
    option2 : int
    option3 : int
    option4 : int
    correctOption : int

class Options(CreateAndUpdateOptions):
    id : int

    class Config:
        orm_mode = True

class PaginatedOptions(BaseModel):
    limit: int
    offset: int
    data: List[Options]
 