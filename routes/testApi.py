from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from exceptions.testExceptions import TestNotFoundError
from repository.responceRepository import get_total_marks
from repository.testRepository import *
from config.database import get_db
from exceptions.optionsExceptions import OptionsInfoException
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
def get_user_by_email(id: int, session: Session = Depends(get_db)):
    try:
        user_info = get_test_by_id(session, id)
        return user_info
    except TestNotFoundError as cie:
        raise HTTPException(**cie.__dict__)

@router.get("/upcoming-test-list")
def upcoming_test_list(email: str, session: Session = Depends(get_db)):
    return get_upcoming_test_list(session, email)

@router.get("/prev-test-list")
def prev_test_list(email: str, session: Session = Depends(get_db)):
    prev_test_list = get_prev_test_list(session, email)
    new_prev_test_list = []
    for test in prev_test_list:
        userId = get_user_info_by_email(session, email).id
        obtainedMarks = get_total_marks(session, userId, test.id)
        new_prev_test_list.append({
            "sharableId": test.sharableId,
            "maxMarks": test.maxMarks,
            "passMarks": test.passMarks,
            "startTime": test.startTime,
            "teacherEmail": test.teacherEmail,
            "id": test.id,
            "name": test.name,
            "testType": test.testType,
            "endTime": test.endTime,
            "obtainedMarks" : obtainedMarks
        })

    return new_prev_test_list

@router.get("/upcoming-test-list-teacher")
def upcoming_test_list_teacher(email: str, session: Session = Depends(get_db)):
    return get_upcoming_test_list_teacher(session, email)

@router.get("/prev-test-list-teacher")
def prev_test_list_teacher(email: str, session: Session = Depends(get_db)):
    return get_prev_test_list_teacher(session, email)