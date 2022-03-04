from urllib import response
from fastapi import FastAPI , status, HTTPException
from pydantic import BaseModel 
from typing import List
from database import SessionLocal
import models
class Student(BaseModel):
    student_id:int
    student_F_Name:str
    student_L_Name:str
    gpa:float

    class Config: 
        orm_mode=True

db=SessionLocal()
app = FastAPI()

@app.get('/students',response_model=List[Student],status_code=status.HTTP_201_CREATED)
def get_all_students():
    students=db.query(models.Student).all()
    return students

@app.get('/students/{student_id}',response_model=Student)
def get_an_student(student_id:int):
    student = db.query(models.Student).filter(models.Student.student_id==student_id).first()
    return student

@app.post('/students', response_model=Student, status_code=status.HTTP_201_CREATED)
def create_an_student(req: Student):
    db_student = db.query(models.Student).filter(models.Student.student_F_Name == req.student_F_Name).first()
    if db_student is not None:
        raise HTTPException(status_code=400, detail="Student already exists")

    new_student = models.Student(
    student_F_Name=req.student_F_Name,
    student_L_Name=req.student_L_Name,
    gpa=req.gpa)

    db.add(new_student)
    db.commit()
    return new_student

@app.put('/student/{student_id}',response_model=Student,status_code=status.HTTP_200_OK)
def update_an_student(student_id:int,student:Student):
    student_to_update=db.query(models.Student).filter(models.Student.student_id==student_id).first()
    student_to_update.student_F_Name=student.student_F_Name
    student_to_update.student_L_Name=student.student_L_Name
    student_to_update.gpa=student.gpa
    db.commit()
    return student_to_update


@app.delete('/student/{student_id}')
def delete_student(student_id:int):
    student_to_delete=db.query(models.Student).filter(models.Student.student_id==student_id).first()

    if student_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")

    db.delete(student_to_delete)
    db.commit()
    return student_to_delete