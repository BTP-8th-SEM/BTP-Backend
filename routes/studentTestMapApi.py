from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository.responceRepository import get_total_marks
from repository.studentTestRepository import *
from config.database import get_db
from repository.userRepository import get_users_by_email_list
from analytics.studentData import studentAnalysis
from analytics.connection import dataframes
from analytics.numpyToJSON import np_encoder

router = APIRouter(tags=['map api'])

session: Session = Depends(get_db)        

@router.post("/create_map", response_model=StudentTestMap)
def create_map(map: CreateAndUpdateStudentTestMap, session: Session = Depends(get_db)):
    return create_map_repo(map, session)

@router.get("/getStudents")
def getStudent(testId: int, session: Session = Depends(get_db)):
    analysis = studentAnalysis(dataframes()).getStudentsList(testId)
    new_list = []
    for student in analysis:
        new_list.append({key:np_encoder(value) for key,value in student.items()})
     
    return new_list