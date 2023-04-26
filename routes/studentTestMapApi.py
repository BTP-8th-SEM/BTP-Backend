from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository.responceRepository import get_total_marks
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
    users_list = get_users_by_email_list(session, id_list)
    new_users_list = []
    for user in users_list:
        new_users_list.append({
            "lastName": user.firstName,
            "id": user.id,
            "role": user.role,
            "email":user.email,
            "firstName": user.firstName,
            # "password": user.password,
            "profilePicUrl":user.profilePicUrl,
            "obtainedMarks":get_total_marks(session,user.id,testId),
            })
        # print(get_total_marks(session, user.id, testId))
     
    return new_users_list