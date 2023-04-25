from typing import List
from sqlalchemy.orm import Session
from exceptions.optionsExceptions import OptionsInfoNotFoundError
from model.optionsModel import McqOptionsInfo
from schema.optionsSchema import CreateAndUpdateOptions


# Function to get list of car info
def get_all_options(session: Session, limit: int, offset: int) -> List[McqOptionsInfo]:
    return session.query(McqOptionsInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular car
def get_options_by_id(session: Session, _id: int) -> McqOptionsInfo:
    options_info = session.query(McqOptionsInfo).get(_id)

    if options_info is None:
        raise OptionsInfoNotFoundError

    return options_info


# Function to add a new car info to the database
def create_option(session: Session, options_info: CreateAndUpdateOptions) -> McqOptionsInfo:
    new_options_info = McqOptionsInfo(**options_info.dict())
    session.add(new_options_info)
    session.commit()
    session.refresh(new_options_info)
    return new_options_info