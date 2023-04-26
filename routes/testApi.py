from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from exceptions.testExceptions import TestNotFoundError
from repository.responceRepository import get_total_marks
from repository.testRepository import *
from config.database import get_db
from exceptions.optionsExceptions import OptionsInfoException
from repository.userRepository import get_user_info_by_email
from repository.userRepository import get_user_info_by_email
from schema.testSchema import Test, CreateAndUpdateTest, PaginatedTest

router = APIRouter(tags=['test Apis'])

@cbv(router)
class Answers:
    session: Session = Depends(get_db)

    @router.get("/getTests", response_model=PaginatedTest)
    def list_users(self, limit: int = 10, offset: int = 0):
        test_list = get_all_tests(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": test_list}
        return response

    @router.post("/createTest")
    def create_test(self, test_info: CreateAndUpdateTest):
        try:
            test_info = create_test(self.session, test_info)
            return test_info
        except OptionsInfoException as cie:
            raise HTTPException(**cie.__dict__)
        
@router.get("/getTestById/{id}")
def get_test_by_id(id: int, session: Session = Depends(get_db)):
    try:
        test_info = get_test_by_id_repo(session, id)
        return test_info
    except TestNotFoundError as cie:
        raise HTTPException(**cie.__dict__)

@router.get("/upcoming-test-list")
def upcoming_test_list(email: str, session: Session = Depends(get_db)):
    return get_upcoming_test_list(session, email)

@router.get("/prev-test-list")
def prev_test_list(email: str, session: Session = Depends(get_db)):
    user = get_user_info_by_email(session, email).id
    list = get_prev_test_list(session, email)

    new_test_list = []
    for test in list:
        obtainedMarks = get_total_marks(session, user, test.id)
        new_test_list.append({
            "name": test.name,
            "teacherEmail": test.teacherEmail,
            "passMarks": test.passMarks,
            "testType": test.testType,
            "endTime": test.endTime,
            "sharableId": test.sharableId,
            "maxMarks": test.maxMarks,
            "id": test.id,
            "startTime": test.startTime,
            "studentId" : user,
            "obtainedMarks" : obtainedMarks
        })

    return new_test_list

@router.get("/upcoming-test-list-teacher")
def upcoming_test_list_teacher(email: str, session: Session = Depends(get_db)):
    return get_upcoming_test_list_teacher(session, email)

@router.get("/prev-test-list-teacher")
def prev_test_list_teacher(email: str, session: Session = Depends(get_db)):
    return get_prev_test_list_teacher(session, email)