from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Student Management API")

# Temporary in-memory database
students = {
    1: {"id": 1, "name": "Rahul", "age": 21, "course": "AI"},
    2: {"id": 2, "name": "Priya", "age": 22, "course": "Data Science"}
}


# Pydantic model: validates incoming student data
class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=16, le=100)
    course: str = Field(min_length=2, max_length=50)


# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


# GET: retrieve all students
@app.get("/students")
def get_students(
    course: Optional[str] = None,
    limit: int = 10
):
    result = list(students.values())

    if course:
        result = [student
             for student in result
            if student["course"].lower() == course.lower()
        ]

    return result[:limit]


# GET: retrieve one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


# POST: create a student
@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    new_id = max(students.keys(), default=0) + 1

    new_student = {
        "id": new_id,
        **student.model_dump()
    }

    students[new_id] = new_student

    return {
        "message": "Student created successfully",
        "student": new_student
    }


# PUT: update an existing student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updated_student = {
        "id": student_id,
        **student.model_dump()
    }

    students[student_id] = updated_student

    return {
        "message": "Student updated successfully",
        "student": updated_student
    }


# DELETE: remove a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }