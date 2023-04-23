from typing import List
from sqlalchemy.orm import Session
from exceptions.answerExceptions import AnswerInfoNotFoundError
from model.answerModel import McqAnswerInfo
from schema.answerSchema import CreateAndUpdateAnswer


# Function to get list of car info
def get_all_answers(session: Session, limit: int, offset: int) -> List[McqAnswerInfo]:
    return session.query(McqAnswerInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular car
def get_answer_by_id(session: Session, _id: int) -> McqAnswerInfo:
    answer_info = session.query(McqAnswerInfo).get(_id)

    if answer_info is None:
        raise AnswerInfoNotFoundError

    return answer_info


# Function to add a new car info to the database
def create_answer(session: Session, answer_info: CreateAndUpdateAnswer) -> McqAnswerInfo:
    new_answer_info = McqAnswerInfo(**answer_info.dict())
    session.add(new_answer_info)
    session.commit()
    session.refresh(new_answer_info)
    return new_answer_info