from pydantic import BaseModel
from typing import List

class CreateAndUpdateOptions(BaseModel):
    option1 : str
    option2 : str
    option3 : str
    option4 : str
    correctOption : int

class Options(CreateAndUpdateOptions):
    id : int

    class Config:
        orm_mode = True

class PaginatedOptions(BaseModel):
    limit: int
    offset: int
    data: List[Options]
 