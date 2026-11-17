from fastapi import FastAPI
app = FastAPI()  # create fastapi appli
@app.get("/")    # first end point
def home(): 
    return {
        "message":"Welcome to Fastapi",
        "goal" : "AI/ML Engineer"
    }
# About endpoint 
@app.get("/about")
def about():
    return {
        "name":"Fastapi",
        "technology" : "Fastapi",
        "purpose" : "Learning Api development"
    }
# health check end point 
@app.get("/health")
def health_check():
    return {
        "status" :"healthy"
    }