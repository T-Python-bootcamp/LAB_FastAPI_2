from pydantic import BaseModel
from typing import Optional,List
from fastapi import FastAPI,status, HTTPException
from database import SessionLocal
import models

app = FastAPI()


class Student(BaseModel):
    id: int
    fname: str
    lname: str
    gpa: float
    
    class Config: # serialize our sql obj to json
        orm_mode=True
db=SessionLocal()


@app.post('/students', response_model=Student, status_code=status.HTTP_201_CREATED)
def create_a_student(student: Student):
    db_student = db.query(models.Student).filter(models.Student.id ==student.id).first()
    if db_student is not None:
        raise HTTPException(status_code=400, detail="Student already exists")
    new_student = models.Student(
        id=student.id,
        fname=student.fname,
        lname=student.lname,
        gpa=student.gpa,
        
        )
    db.add(new_student)
    db.commit()
    return new_student

@app.get('/students', response_model=List[Student],status_code=200)
def get_all_students():
    students=db.query(models.Student).all()
    return students

@app.put('/student/{student_id}',response_model=Student,status_code=status.HTTP_200_OK)
def update_an_student(student_id:int,student:Student):
    student_to_update=db.query(models.Student).filter(models.Student.id==student_id).first()
    student_to_update.fname=student.fname
    student_to_update.lname=student.lname
    student_to_update.gpa=student.gpa
    db.commit()
    
    return student_to_update

@app.delete('/student/{student_id}')
def delete_student(student_id:int):
    student_to_delete=db.query(models.Student).filter(models.Student.id==student_id).first()
    if student_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    db.delete(student_to_delete)
    db.commit()
    return student_to_delete
