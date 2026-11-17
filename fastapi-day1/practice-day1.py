from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class House(BaseModel) :
    area : int
    bedrooms : int 


@app.get("/profile")
def profile():
    return {
        "name" : "priya",
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
def predict( data: House ):
    return {
        "area_of_house" : data.area *30000 + data.bedrooms *20000
    }
