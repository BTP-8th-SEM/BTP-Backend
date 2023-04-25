from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from config.database import Base

class StudentTestMapInfo(Base):
    __tablename__ = "student_test_map"

    id = Column(Integer, primary_key=True, index=True)
    userEmail = Column(String)
    testId = Column(Integer)