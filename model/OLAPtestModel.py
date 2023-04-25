from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from config.database import Base

class OLAPTestInfo(Base):
    __tablename__ = "olap_test"

    id = Column(Integer, primary_key=True, index=True)
    testId = Column(Integer)
    totalAppeared = Column(Integer)
    maxMarks = Column(Integer)
    highestMarks = Column(Integer)
    lowestMarks = Column(Integer)
    avgMarks = Column(Integer)
    noOfPassed = Column(Integer)
    noOfFailed = Column(Integer)
    lastUpdated = Column(String)
