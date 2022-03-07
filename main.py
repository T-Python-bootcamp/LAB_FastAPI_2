from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from passlib.hash import pbkdf2_sha256
from sqlalchemy import select, update, delete

from database import SessionLocal
import models 

class Student(BaseModel):
    ID: int
    F_Name: str
    L_Name: str
    GPA: float
    
    class Config:
        orm_mode=True

db = SessionLocal()

app = FastAPI()

@app.post("/student")
async def add_student(student: Student):
    student = models.Student(
        ID = student.ID,
        F_Name = student.F_Name,
        L_Name = student.L_Name,
        GPA = student.GPA
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return f"Student {student.ID} is successfully added"


@app.get("/student")
async def get_student(ID):
    student = db.execute(select(models.Student).where(models.Student.ID == ID)).fetchone()
    if student:
        return student
    else:
        return f"Provided student ({id}) is not exist"


@app.put("/student")
async def update_student(student: Student):
    id = db.execute(select(models.Student).where(models.Student.ID == student.ID)).fetchone()
    if id:
        db.execute(update(models.Student).where(models.Student.ID == student.ID).\
        values(F_Name = student.F_Name, L_Name = student.L_Name, GPA = student.GPA))
        db.commit()

        return f"Student {student.ID} is successfully updated"
    else:
        raise HTTPException(status_code = 404, detail = f"Provided student ({student.ID}) is not exist")


@app.delete("/student")
async def delete_student(ID: int = Body(...)):
    student = db.execute(select(models.Student.ID).where(models.Student.ID == ID)).fetchone()
    if student:
        db.execute(delete(models.Student).where(models.Student.ID == ID))
        db.commit()
        return f"Student {ID} is successfully deleted"
    else:
        return f"Provided student ({ID}) is not exist"
    
