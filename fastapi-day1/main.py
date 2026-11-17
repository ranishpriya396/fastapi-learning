from fastapi import FastAPI
app = FastAPI()
@app.get("/student/{student_id}")
def get_student(student_id : int):
    return {
        "student_name" : "Priya",
        "student_id" : student_id
    }