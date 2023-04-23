from pydantic import BaseModel
from typing import Optional, List
from model.userModel import UserType

class CreateAndUpdateUser(BaseModel):
    email : str
    firstName : str
    lastName : str
    password : str
    role : UserType
    profilePicUrl : str

class User(CreateAndUpdateUser):
    id : int

    class Config:
        orm_mode = True

class PaginatedUserInfo(BaseModel):
    limit: int
    offset: int
    data: List[User]
 