from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/profile")
def profile():
    return {
        "name" : "priya"
        "role" : "developer",
        "skills" :"c++ , c#"
    }
@app.get("/predict-demo")
def predict_demo():
    return {
        "model" : "Linear regression",
        "prediction" : 4500000,
        "status" : "success"
    }
@app.post("/predict")
def predict(area : int , bedrooms: int ):
    return {
        area : area,
        bedrooms : bedrooms
    }
