from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository.studentTestRepository import *
from config.database import get_db

router = APIRouter()

session: Session = Depends(get_db)        

@router.post("/create_map", response_model=StudentTestMap)
def create_map(map: CreateAndUpdateStudentTestMap, session: Session = Depends(get_db)):
    return create_map_repo(map, session)