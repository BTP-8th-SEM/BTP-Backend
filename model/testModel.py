from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from model.questionModel import AnswerType
from config.database import Base
import enum

class Test(Base):
    __tablename__ = "test_db"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    maxMarks = Column(Integer)
    passMarks = Column(Integer)
    testType = Column(Enum(AnswerType))
    startTime = Column(String)
    endTime = Column(String)