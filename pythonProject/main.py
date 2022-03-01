from typing import List
from fastapi import FastAPI,status, HTTPException
import models
from pydantic import BaseModel
from database import SessionLocal


app = FastAPI()

class student(BaseModel):
    ID: int
    F_Name: str
    L_Name: str
    GPA: float

    class Config:  # serialize our sql obj to json
        orm_mode = True

db = SessionLocal()

@app.get('/students', response_model=List[student],status_code=200)
def get_all_students():
    students = db.query(models.Student).all()
    return students

@app.post('/students', response_model=student, status_code=status.HTTP_201_CREATED)
def create_an_item(student: student):
    db_student = db.query(models.Student).filter(models.Student.F_Name == student.F_Name).first()

    if db_student is not None:
        raise HTTPException(status_code=400, detail="student already exists")

    new_student = models.Student(
        F_Name=student.F_Name,
        L_Name=student.L_Name,
        GPA=student.GPA
        )
    db.add(new_student)
    db.commit()
    return new_student

@app.put('/student/{student_id}',response_model=student,status_code=status.HTTP_200_OK)
def update_an_item(student_id:int,student:student):
    student_to_update=db.query(models.Student).filter(models.Student.ID==student_id).first()

    student_to_update.F_Name=student.F_Name
    student_to_update.L_Name=student.L_Name
    student_to_update.GPA=student.GPA
    db.commit()
    return student_to_update

@app.delete('/student/{student_id}')

def delete_item(student_id:int):
    student_to_delete=db.query(models.Student).filter(models.Student.ID==student_id).first()
    if student_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    else:
        db.delete(student_to_delete)
        db.commit()
        return student_to_delete