from database import Base
from sqlalchemy import String, Float, Integer, Column
class Student(Base): # inherets from Base class
    __tablename__ = 'Student'
    F_Name = Column(String(255), nullable=False, unique=True)
    L_Name = Column(String(255), nullable=False, unique=False)
    ID = Column(Integer, primary_key=True)
    GPA = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Student name={self.F_Name} ID={self.ID}>"