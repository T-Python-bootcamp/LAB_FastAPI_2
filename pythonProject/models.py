from database import Base
from sqlalchemy import String, Float, Integer, Column, Text

class Student(Base):
    __tablename__ = 'Student'
    ID = Column(Integer, primary_key=True)
    F_Name = Column(String(255), nullable=False, unique=True)
    L_Name = Column(String)
    GPA = Column(Float, nullable=False)


def __repr__(self):
    return f"<Item name={self.F_Name} ID={self.ID}>"
