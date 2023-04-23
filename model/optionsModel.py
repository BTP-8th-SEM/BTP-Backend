from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from config.database import Base

class McqOptionsInfo(Base):
   __tablename__ = "mcq_options"

   id = Column(Integer, primary_key=True, index=True)
   option1 = Column(Integer);
   option2 = Column(Integer);
   option3 = Column(Integer);
   option4 = Column(Integer);
   correctOption = Column(Integer);