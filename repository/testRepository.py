from typing import List
from sqlalchemy.orm import Session
from exceptions.optionsExceptions import OptionsInfoNotFoundError
from model.testModel import TestInfo
from schema.testSchema import *


# Function to get list of car info
def get_all_tests(session: Session, limit: int, offset: int) -> List[TestInfo]:
    return session.query(TestInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular car
# def get_options_by_id(session: Session, _id: int) -> McqOptionsInfo:
#     options_info = session.query(McqOptionsInfo).get(_id)

#     if options_info is None:
#         raise OptionsInfoNotFoundError

#     return options_info


# Function to add a new car info to the database
def create_test(session: Session, tests_info: CreateAndUpdateTest) -> TestInfo:
    new_tests_info = TestInfo(**tests_info.dict())
    session.add(new_tests_info)
    session.commit()
    session.refresh(new_tests_info)
    return new_tests_info