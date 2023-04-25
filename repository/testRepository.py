from typing import List
from sqlalchemy.orm import Session
from exceptions.testExceptions import TestNotFoundError
from model.testModel import TestInfo
from repository.studentTestRepository import get_all_map_email
from schema.testSchema import *
import string, random
from datetime import datetime

def get_all_tests(session: Session, limit: int, offset: int) -> List[TestInfo]:
    return session.query(TestInfo).offset(offset).limit(limit).all()

def get_test_by_id(session: Session, id: int) -> TestInfo:
    test_info = session.query(TestInfo).get(id)

    if test_info is None:
        raise TestNotFoundError

    return test_info

def get_upcoming_test_list(session: Session, email: str) -> List[TestInfo]:
    map_list = get_all_map_email(session, email)
    list_test_id = [map_info.testId for map_info in map_list]
    test_list = get_tests_list(session, list_test_id)
    upcoming_test_list = list(filter(lambda testInfo:diffTimePositive(testInfo.endTime), test_list))
    return upcoming_test_list

def get_prev_test_list(session: Session, email: str) -> List[TestInfo]:
    map_list = get_all_map_email(session, email)
    list_test_id = [map_info.testId for map_info in map_list]
    test_list = get_tests_list(session, list_test_id)
    prev_test_list = list(filter(lambda testInfo:diffTimePositive(testInfo.endTime)==False, test_list))
    return prev_test_list

def get_upcoming_test_list_teacher(session: Session, email: str) -> List[TestInfo]:
    return None

def get_prev_test_list_teacher(session: Session, email: str) -> List[TestInfo]:
    return None

def get_tests_list(session: Session, id_list: List[int]) -> List[TestInfo]:
    test_list = list(filter(lambda testInfo:testInfo.id in id_list, session.query(TestInfo).all()))
    print(test_list)
    return test_list

def create_test(session: Session, tests_info: CreateAndUpdateTest) -> TestInfo:
    new_tests_info = TestInfo(**tests_info.dict())
    new_tests_info.sharableId = generate()
    session.add(new_tests_info)
    session.commit()
    session.refresh(new_tests_info)
    return new_tests_info

def generate() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))

def diffTimePositive(time: str) -> bool:
    now = datetime.now().strftime("%d-%m-%Y %H:%M %p")
    dtNow = datetime.strptime(now, "%d-%m-%Y %H:%M %p")
    dtGiven = datetime.strptime(time, "%d-%m-%Y %H:%M %p")

    return (dtGiven - dtNow).total_seconds() >= 0