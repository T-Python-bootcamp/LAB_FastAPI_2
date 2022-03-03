from database import Base
from sqlalchemy import String, Float, Integer, Column, Text, ForeignKey
from sqlalchemy.orm import relationship


class Item(Base): # inherets from Base class
    __tablename__ = 'items'
    student_id = Column(Integer, primary_key=True)
    student_F_Name = Column(String(255), nullable=False, unique=True)
    student_L_Name = Column(String(255), nullable=False, unique=True)
    gpa = Column(Float, nullable=False)

    

    def __repr__(self):
        return f"<Item name={self.student_F_Name} price={self.GPA}>"

