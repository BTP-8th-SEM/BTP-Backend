from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from repository.studentTestRepository import *
from schema.testSchema import PaginatedTest
from config.database import get_db

router = APIRouter()

session: Session = Depends(get_db)        

@router.get("/test_list_email", response_model=PaginatedTest)
def test_list_email(user_email: str, session: Session = Depends(get_db)):
    list_test = get_test_list_email(session, user_email)
    obj = PaginatedTest()
    obj.data = list_test
    return obj

@router.post("/create_map", response_model=StudentTestMap)
def create_map(map: CreateAndUpdateStudentTestMap, session: Session = Depends(get_db)):
    return create_map_repo(map, session)