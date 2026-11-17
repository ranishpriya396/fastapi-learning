from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title = "Day 1 FastAPI Practice")

class Student(BaseModel):
    name : str 
    age : int 
    course : str 

#Post request with json body
@app.post("/student",status_code = 200)
def create_student(student : Student):
    return {
        "message" : "student added", 
        "student_data" : student 
    }

# Path Parameter
@app.get("/student/{student_id}")
def get_student(student_id : int):
    return {
        "student_name" : "Priya",
        "student_id" : student_id
    }