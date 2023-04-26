from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repository.userRepository import *
from config.database import get_db
from exceptions.userExceptions import UserInfoException
from schema.userSchema import User, CreateAndUpdateUser, PaginatedUserInfo
from schema.AuthenticationResponse import AuthenticationResponse

router = APIRouter(tags=['user apis'])

@cbv(router)
class Users:
    session: Session = Depends(get_db)

    @router.get("/getUsers", response_model=PaginatedUserInfo)
    def list_users(self, limit: int = 10, offset: int = 0):

        users_list = get_all_users(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": users_list}

        return response

    @router.post("/signUp")
    def add_user(self, user_info: CreateAndUpdateUser):
        try:
            user_info = create_user(self.session, user_info)
            return user_info
        except UserInfoException as cie:
            raise HTTPException(**cie.__dict__)
        
@router.get("/login", response_model=AuthenticationResponse)
def login(user_email: str, password: str, session: Session = Depends(get_db)):
    try:
        user_info = get_user_info_by_email(session, user_email)
        if(user_info.password == password):
            authResponse = AuthenticationResponse()
            authResponse.role = user_info.role
            authResponse.isAuthenticated = True
            return authResponse
        else :
            authResponse = AuthenticationResponse()
            authResponse.role = None
            authResponse.isAuthenticated = False
            return authResponse
    except UserInfoException as cie:
        raise HTTPException(**cie.__dict__)
    
@router.get("/getUserByEmail/{user_email}", response_model=User)
def get_user_by_email(user_email: str, session: Session = Depends(get_db)):
    try:
        user_info = get_user_info_by_email(session, user_email)
        return user_info
    except UserInfoException as cie:
        raise HTTPException(**cie.__dict__)

@router.get("/getUser/{user_id}", response_model=User)
def get_user_info(user_id: int, session: Session = Depends(get_db)):

    try:
        user_info = get_user_info_by_id(session, user_id)
        return user_info
    except UserInfoException as cie:
        raise HTTPException(**cie.__dict__)


# @router.put("/updateUser/{email_id}", response_model=User)
# def update_User(email_id: str, new_info: CreateAndUpdateUser, session: Session = Depends(get_db)):

#     try:
#         user_info = update_user_info(session, email_id, new_info)
#         return user_info
#     except UserInfoException as cie:
#         raise HTTPException(**cie.__dict__)


# @router.delete("/deleteUser/{email_id}")
# def delete_user(email_id: str, session: Session = Depends(get_db)):

#     try:
#         return delete_user_info(session, email_id)
#     except UserInfoException as cie:
#         raise HTTPException(**cie.__dict__)