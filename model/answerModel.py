from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from config.database import Base

class McqAnswerInfo(Base):
   __tablename__ = "maq_answers"

   id = Column(Integer, primary_key=True, index=True)
   option1 = Column(Integer);
   option2 = Column(Integer);
   option3 = Column(Integer);
   option4 = Column(Integer);
   CorrectOption = Column(Integer);