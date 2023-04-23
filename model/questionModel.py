from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from config.database import Base
import enum

class AnswerType(str, enum.Enum):
    MCQ = "MCQ"
    Subjective = "Subjective"

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    maxMarks = Column(Integer)
    answerType = Column(Enum(AnswerType))
    answerId = Column(Integer)
