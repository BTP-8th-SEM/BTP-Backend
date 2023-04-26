from fastapi import APIRouter, Depends
from analytics.OLAP import run_OLAP_Test
from analytics.studentData import studentAnalysis
from analytics.connection import dataframes
from analytics.numpyToJSON import np_encoder
from repository.questionRepository import get_question_list
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

@router.get("/getQuestionVSMarks/{testId}/{studentId}")
def get_user_by_email(testId: int, studentId: int, session: Session = Depends(get_db)):
   list_question = get_question_list(session, testId)
   new_list = []
   for question in list_question :
      data = studentAnalysis(dataframes()).getQuestionData(testId, studentId, question.id)
      print(data)
      data1 =  {
        "questionId": question.id,
        "averageMarks": 50,
        "yourMarks": 75,
        "highestMarks": 100,
        "lowestMarks": 20
      }
      new_list.append(data1)
   return new_list
   



