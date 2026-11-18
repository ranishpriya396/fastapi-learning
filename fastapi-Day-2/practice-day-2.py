from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Helloworld"
    }

@app.get("/about")
def about():
    return {
        "message" : "I am learning FastAPI",
        "day": 2
    }

@app.get("/contact")
def contract():
    return{
        "email" : "student@gamil.com",
        "message" : "Contact me"
    }
