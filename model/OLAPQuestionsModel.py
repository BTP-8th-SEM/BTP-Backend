from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from config.database import Base

class OLAPQuestionInfo(Base):
    __tablename__ = "olap_question"

    id = Column(Integer, primary_key=True, index=True)
    questionId = Column(Integer)
    maxMarks = Column(Integer)
    highestMarks = Column(Integer)
    lowestMarks = Column(Integer)
    avgMarks = Column(Integer)
    topic = Column(String) 