from database import Base
from sqlalchemy import String, Integer, Float, Column


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=False)
    gpa = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return f"<Student id={self.id} name={self.firstName}>"
