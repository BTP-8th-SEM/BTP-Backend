from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from config.database import Base

class McqOptionsInfo(Base):
   __tablename__ = "mcq_options"

   id = Column(Integer, primary_key=True, index=True)
   option1 = Column(String);
   option2 = Column(String);
   option3 = Column(String);
   option4 = Column(String);
   correctOption = Column(String);