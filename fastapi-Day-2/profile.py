from fastapi import FastAPI
from pydantic  import BaseModel

class Profile(BaseModel): 
    name : str     # remeber not need the "   "  while defining the variable inside the class
    phone_no : int
    email : str 
app = FastAPI()
@app.post("/profile")       # here you accept profile data -use :post method
def profile(data : Profile):  ## Mistake occured , but now corrected 
    return {
        "name" : data.name ,
        "Phone No." : data.phone_no,
        "email" : data.email
    }
