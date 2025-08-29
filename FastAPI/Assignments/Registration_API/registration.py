from pydantic import BaseModel, EmailStr, Field
from fastapi import FastAPI, HTTPException

fastapp = FastAPI()

USERS = {}
EMAILS = []
IDs = []

class RegistrationModel(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=8)

@fastapp.post("/register")
def register(model: RegistrationModel):
    if model.email in EMAILS:
        raise HTTPException(status_code=400, detail="You've already subscribed")
    elif model.username in IDs:
        raise HTTPException(status_code=400, detail="User Name is already in Use, Choose another one")
    USERS[model.email] = model.__dict__
    EMAILS.append(model.email)
    IDs.append(model.username)
    return {"response": "Register Successfully !!!"}

@fastapp.post("/clear")
def clear():
    global USERS
    USERS = {}
    return {"response": "Users List cleared Successfully !!"}
    
@fastapp.post("/users")
def get_users():
    return list(USERS.values())