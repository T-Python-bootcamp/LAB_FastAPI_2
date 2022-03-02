from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import SessionLocal
from typing import List
import models

app = FastAPI()


class Student(BaseModel):
    id: int
    firstName: str
    lastName: str
    gpa: float

    class Config:
        orm_mode = True  # https://pydantic-docs.helpmanual.io/usage/models/#orm-mode-aka-arbitrary-class-instances


db = SessionLocal()


# Endpoint To test pydantic
# @app.get("/stusents")
# def root(student: Student):
#     return {
#         "First Name": student.first_name,
#         "Last Name": student.last_name,
#         "GPA": student.gpa
#     }


# << CRUD Operations on Student Schema >>


# Enpoint to get Students
@app.get("/allStudents", response_model=List[Student], status_code=status.HTTP_200_OK)
def get_all_students():
    studens = db.query(models.Student).all()
    return studens


# Enpoint to get student by student id
@app.get("/student/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def get_student(student_id: int):
    student = db.query(models.Student).filter(
        models.Student.id == student_id).first()
    return student


# Enpoint to create student
@app.post("/createStudent", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    new_student = models.Student(
        firstName=student.firstName,
        lastName=student.lastName,
        gpa=student.gpa
    )

    db.add(new_student)
    db.commit()
    return new_student


# Enpoint to update student by student id
@app.put("/student/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def update_student(student_id: int, student: Student):
    student_update = db.query(models.Student).filter(
        models.Student.id == student_id).first()
    student_update.firstName = student.firstName
    student_update.lastName = student.lastName
    student_update.gpa = student.gpa

    db.commit()
    return student_update


# Enpoint to delete student by student id
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    student_delete = db.query(models.Student).filter(
        models.Student.id == student_id).first()
    if student_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student Not found")

    db.delete(student_delete)
    db.commit()
    return {"message": "Deleted Sucsessfully..."}
