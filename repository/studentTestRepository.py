from typing import List
from sqlalchemy.orm import Session
# from exceptions.optionsExceptions import OptionsInfoNotFoundError
from model.studentTestMap import StudentTestMapInfo
# from model.testModel import TestInfo
# from repository.testRepository import get_tests_list
from schema.studentTestMapSchema import *
import string, random


# Function to get list of car info
def get_all_maps(session: Session, limit: int, offset: int) -> List[StudentTestMapInfo]:
    return session.query(StudentTestMapInfo).offset(offset).limit(limit).all()

def get_all_map_email(session: Session, email: str) -> List[StudentTestMapInfo]:
    return session.query(StudentTestMapInfo).filter(StudentTestMapInfo.userEmail == email).all()

# def get_test_list_email(session: Session, userEmail: str) -> List[TestInfo]:
#     list_test_info = get_all_map_email(session, userEmail)
#     print(list_test_info)
#     list_test_id = [test_info.testId for test_info in list_test_info]
#     print(list_test_id)
#     return get_tests_list(session, list_test_id)

def create_map_repo(map: CreateAndUpdateStudentTestMap, session: Session) -> StudentTestMapInfo:
    new_map_info = StudentTestMapInfo(**map.dict())
    session.add(new_map_info)
    session.commit()
    session.refresh(new_map_info)
    return new_map_info

def generate() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))

