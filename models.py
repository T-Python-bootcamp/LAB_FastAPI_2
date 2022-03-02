from database import Base
from sqlalchemy import String, Float, Integer, Column, Text

class Student(Base): # inherets from Base class
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fname = Column(String(255), nullable=False, unique=False)
    lname = Column(String(255), nullable=False, unique=False)
    gpa = Column(Float, nullable=False)
    def __repr__(self):
        return f"<Student first name={self.fname} last name= {self.lname} gpa={self.gpa}>"
