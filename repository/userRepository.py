from typing import List
from sqlalchemy.orm import Session
from exceptions.userExceptions import UserInfoInfoAlreadyExistError, UserInfoNotFoundError
from model.userModel import UserInfo
from schema.userSchema import CreateAndUpdateUser


# Function to get list of car info
def get_all_users(session: Session, limit: int, offset: int) -> List[UserInfo]:
    return session.query(UserInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular car
def get_user_info_by_id(session: Session, _id: int) -> UserInfo:
    user_info = session.query(UserInfo).get(_id)

    if user_info is None:
        raise UserInfoNotFoundError

    return user_info

def get_user_info_by_email(session: Session, email: str) -> UserInfo:
    user_info = session.query(UserInfo).filter(UserInfo.email == email).first()

    if user_info is None:
        raise UserInfoNotFoundError

    return user_info


# Function to add a new car info to the database
def create_user(session: Session, user_info: CreateAndUpdateUser) -> UserInfo:
    user_details = session.query(UserInfo).filter(UserInfo.email == user_info.email).first()
    if user_details is not None:
        raise UserInfoInfoAlreadyExistError

    new_user_info = UserInfo(**user_info.dict())
    session.add(new_user_info)
    session.commit()
    session.refresh(new_user_info)
    return new_user_info


# Function to update details of the car
def update_user_info(session: Session, email: str, info_update: CreateAndUpdateUser) -> UserInfo:
    user_info = get_user_info_by_email(session, email)

    if user_info is None:
        raise UserInfoNotFoundError

    user_info.email = info_update.email
    user_info.firstName = info_update.firstName
    user_info.lastName = info_update.lastName
    user_info.password = info_update.password
    user_info.role = info_update.role
    user_info.profilePicUrl = info_update.profilePicUrl

    session.commit()
    session.refresh(user_info)

    return user_info


# Function to delete a car info from the db
def delete_user_info(session: Session, email: str):
    user_info = get_user_info_by_email(session, email)

    if user_info is None:
        raise UserInfoNotFoundError

    session.delete(user_info)
    session.commit()

    return
