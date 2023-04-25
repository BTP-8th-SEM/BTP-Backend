from pydantic import BaseModel
from typing import Optional
from model.userModel import UserType

class AuthenticationResponse(BaseModel):
    isAuthenticated : Optional[bool] = False
    role : Optional[UserType] = None

    class Config:
        orm_mode = True