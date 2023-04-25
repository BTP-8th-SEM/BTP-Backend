from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from exceptions.testExceptions import TestNotFoundError
from repository.testRepository import *
from config.database import get_db
from exceptions.optionsExceptions import OptionsInfoException
from schema.testSchema import Test, CreateAndUpdateTest, PaginatedTest

router = APIRouter()

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
    return get_prev_test_list(session, email)

@router.get("/upcoming-test-list-teacher")
def upcoming_test_list_teacher(email: str, session: Session = Depends(get_db)):
    return get_upcoming_test_list_teacher(session, email)

@router.get("/prev-test-list-teacher")
def prev_test_list_teacher(email: str, session: Session = Depends(get_db)):
    return get_prev_test_list_teacher(session, email)