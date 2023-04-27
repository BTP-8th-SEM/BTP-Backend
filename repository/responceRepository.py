from sqlalchemy.orm import Session

from model.responsesModel import ResponsesInfo
import json 

def get_total_marks(session: Session, userId: int, testId: int) -> int:
    response_list = session.query(ResponsesInfo).filter(ResponsesInfo.userId == userId and ResponsesInfo.testId == testId).all()
    totalMarks = 0
    for i in response_list:
        totalMarks += i.obtainedMarks
    return totalMarks

def set_respones_by_id(session: Session, userId: int) :
    new_list = session.query(ResponsesInfo).filter(ResponsesInfo.userId == 2).all()
    new_list_2 = []
    for info in new_list:
        responce = ResponsesInfo()
        responce.questionId = info.questionId
        responce.userId = userId
        responce.body = info.body
        responce.testId = info.testId
        responce.obtainedMarks = info.obtainedMarks
        print(responce)
        session.add(responce)
        session.commit()
        session.refresh(responce)
        new_list_2.append(responce)
    
    return new_list_2