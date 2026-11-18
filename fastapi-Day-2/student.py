from fastapi import FastAPI 
from pydantic import BaseModel , Field 

app = FastAPI()
class Student(BaseModel):
    name : str = Field(max_length = 32 , min_length= 4 )
    age : int = Field(ge = 12 , le = 34)
    course : str = Field(max_length=21 , min_length = 4)

@app.post("/student")
def create_student(student : Student):
    return {
        "name": student.name,
        "age" : student.age,
        "course" : student.course
    }