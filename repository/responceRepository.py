from sqlalchemy.orm import Session

from model.responsesModel import ResponsesInfo

def get_total_marks(session: Session, userId: int, testId: int) -> int:
    response_list = session.query(ResponsesInfo).filter(ResponsesInfo.userId == userId and ResponsesInfo.testId == testId).all()
    totalMarks = 0
    for i in response_list:
        totalMarks += i.obtainedMarks
    return totalMarks