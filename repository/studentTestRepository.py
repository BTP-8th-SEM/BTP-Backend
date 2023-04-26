from typing import List
from sqlalchemy.orm import Session
from model.studentTestMap import StudentTestMapInfo
from schema.studentTestMapSchema import *
import string, random


# Function to get list of car info
def get_all_maps(session: Session, limit: int, offset: int) -> List[StudentTestMapInfo]:
    return session.query(StudentTestMapInfo).offset(offset).limit(limit).all()

def get_all_student_ids(session: Session, id: int) -> List[str]:
    return list(map(lambda x:x.userEmail, session.query(StudentTestMapInfo).filter(StudentTestMapInfo.testId == id).all()))

def get_all_map_email(session: Session, email: str) -> List[StudentTestMapInfo]:
    return session.query(StudentTestMapInfo).filter(StudentTestMapInfo.userEmail == email).all()

def create_map_repo(map: CreateAndUpdateStudentTestMap, session: Session) -> StudentTestMapInfo:
    new_map_info = StudentTestMapInfo(**map.dict())
    session.add(new_map_info)
    session.commit()
    session.refresh(new_map_info)
    return new_map_info

def generate() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))

