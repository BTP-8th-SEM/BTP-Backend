from fastapi import APIRouter, Depends
from typing import List
from repository.responceRepository import set_respones_by_id
from repository.userRepository import get_user_info_by_email
from schema.responsesSchema import Response
from sqlalchemy.orm import Session
from config.database import get_db

router = APIRouter(tags=['responce apis'])    
        
@router.get("/setResponses/{email}")
def get_user_by_email(email: str, session: Session = Depends(get_db))->None:
    userId = get_user_info_by_email(session, email).id
    return set_respones_by_id(session, userId)

        