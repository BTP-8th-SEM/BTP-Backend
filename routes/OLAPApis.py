from fastapi import APIRouter, Depends
from analytics.OLAP import run_OLAP_Test
from analytics.studentData import studentAnalysis
from analytics.connection import dataframes
from analytics.numpyToJSON import np_encoder
from repository.testRepository import get_test_by_id_repo
from sqlalchemy.orm import Session
from config.database import get_db

router = APIRouter(tags=['olap apis'])    
        
@router.get("/getAnalysisTestById/{id}")
def get_user_by_email(id: int):
   return run_OLAP_Test(id)

@router.get("/getUserTestAnalysis/{testId}/{studentId}")
def get_user_by_email(testId: int, studentId: int, session: Session = Depends(get_db)):
   data = studentAnalysis(dataframes()).getTestData(testId, studentId)
   name = get_test_by_id_repo(session, testId).name
   print(data)
   new_data = {
      "subjectName": name,
        "averageMarks": data['avgMarks'],
        "yourMarks": data['totalMarksObtained'],
        "highestMarks": data['highestMarks'],
        "lowestMarks": data['lowestMarks'] 
        }
   return [{key:np_encoder(value) for key, value in new_data.items()}]
   



