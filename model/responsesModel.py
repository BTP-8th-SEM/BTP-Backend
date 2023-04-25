from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from config.database import Base

class Question(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    questionId = Column(Integer)
    userId = Column(Integer)
    testId = Column(Integer)
    body = Column(String)
    obtainedMarks = Column(Integer)
