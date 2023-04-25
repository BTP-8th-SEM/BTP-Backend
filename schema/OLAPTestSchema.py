from pydantic import BaseModel
from typing import List

class CreateAndUpdateOLAPTest(BaseModel):
    testId : int
    totalAppeared : int
    maxMarks : int
    highestMarks : int
    lowestMarks : int
    avgMarks : int
    noOfPassed : int
    noOfFailed : int
    lastUpdated : str

class OLAPTest(CreateAndUpdateOLAPTest):
    id : int

    class Config:
        orm_mode = True

class PaginatedOLAPTest(BaseModel):
    limit: int
    offset: int
    data: List[OLAPTest]