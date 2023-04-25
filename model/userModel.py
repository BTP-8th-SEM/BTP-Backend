from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer,Enum
from config.database import Base
import enum

class UserType(str, enum.Enum):
    student = "student"
    teacher = "teacher"

class UserInfo(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    password = Column(String)
    role = Column(Enum(UserType))
    profilePicUrl = Column(String)