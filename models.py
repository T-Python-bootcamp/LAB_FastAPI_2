from database import Base
from sqlalchemy import String, Float, Integer, Column, Text


class Student(Base): # inherets from Base class
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    student_F_Name = Column(String(50), nullable=False)
    student_L_Name = Column(String(50), nullable=False)
    gpa = Column(Float, nullable=False)


    def __repr__(self):
        return f"<Item student_F_Name={self.student_F_Name} gpa={self.gpa}>"