from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repository.userRepository import get_all_users, create_user, get_user_info_by_id, update_user_info, delete_user_info
from config.database import get_db
from exceptions.userExceptions import UserInfoException
from schema.userSchema import User, CreateAndUpdateUser, PaginatedUserInfo

router = APIRouter()

# Example of Class based view
@cbv(router)
class Users:
    session: Session = Depends(get_db)

    # API to get the list of car info
    @router.get("/getUsers", response_model=PaginatedUserInfo)
    def list_users(self, limit: int = 10, offset: int = 0):

        users_list = get_all_users(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": users_list}

        return response

    # API endpoint to add a car info to the database
    @router.post("/addUser")
    def add_user(self, user_info: CreateAndUpdateUser):

        try:
            user_info = create_user(self.session, user_info)
            return user_info
        except UserInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular car
@router.get("/getUser/{user_id}", response_model=User)
def get_user_info(user_id: int, session: Session = Depends(get_db)):

    try:
        user_info = get_user_info_by_id(session, user_id)
        return user_info
    except UserInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing car info
@router.put("/updateUser/{user_id}", response_model=User)
def update_User(user_id: int, new_info: CreateAndUpdateUser, session: Session = Depends(get_db)):

    try:
        user_info = update_user_info(session, user_id, new_info)
        return user_info
    except UserInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a car info from the data base
@router.delete("/deleteUser/{user_id}")
def delete_car(user_id: int, session: Session = Depends(get_db)):

    try:
        return delete_user_info(session, user_id)
    except UserInfoException as cie:
        raise HTTPException(**cie.__dict__)