from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository.studentTestRepository import *
from config.database import get_db
from repository.userRepository import get_users_by_email_list

router = APIRouter(tags=['map api'])

session: Session = Depends(get_db)        

@router.post("/create_map", response_model=StudentTestMap)
def create_map(map: CreateAndUpdateStudentTestMap, session: Session = Depends(get_db)):
    return create_map_repo(map, session)

@router.get("/getStudents")
def getStudent(testId: int, session: Session = Depends(get_db)):
    id_list = get_all_student_ids(session, testId)
    return get_users_by_email_list(session, id_list)