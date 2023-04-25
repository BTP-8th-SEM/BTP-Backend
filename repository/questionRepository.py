from typing import List
from sqlalchemy.orm import Session
from exceptions.questionExceptions import QuestionInfoException
from model.questionModel import Question
from schema.questionSchema import CreateAndUpdateQuestion


# Function to get list of car info
def get_all_questions(session: Session, limit: int, offset: int) -> List[Question]:
    return session.query(Question).offset(offset).limit(limit).all()


# Function to  get info of a particular car
def get_question_by_id(session: Session, _id: int) -> Question:
    question_info = session.query(Question).get(_id)

    if question_info is None:
        raise QuestionInfoException

    return question_info


# Function to add a new car info to the database
def create_question(session: Session, question_info: CreateAndUpdateQuestion) -> Question:
    new_question_info = Question(**question_info.dict())
    session.add(new_question_info)
    session.commit()
    session.refresh(new_question_info)
    return new_question_info