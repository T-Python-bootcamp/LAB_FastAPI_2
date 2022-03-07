from contextlib import nullcontext
from operator import index
from database import Base
from sqlalchemy import String, Integer, Float, Column

class Student(Base):
    __tablename__ = "students"
    ID = Column(Integer, primary_key=True)
    F_Name = Column(String(30), nullable=False)
    L_Name = Column(String(30), nullable=False)
    GPA = Column(Float, nullable=False)

    def __repr__(self):
        return f"Student info\nID: {self.ID}\nName: {self.F_Name} {self.L_Name}\GPA: {self.GPA}"