from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

USER_DB = {
    1:{"name": "Ayush", "age": 27},
    2:{"name": "Piyush", "age": 28},
    3:{"name":"Raju", "age":30}
    
}


class UserModel(BaseModel):
    name: str
    age: int
    

@app.put("/user/update/{user_id}")
def user_update(user_id: int, user: UserModel):
    if user_id in USER_DB:
        USER_DB[user_id] = user.__dict__
        print(f"Users: {USER_DB}")
        return {"message": "User updated successfully", "user": USER_DB[user_id]}
    else:
        return {"message": "User not found"}
    

@app.delete("/user/delete/{user_id}")
def user_update(user_id: int):
    if user_id in USER_DB:
        del USER_DB[user_id]
        print(f"Users: {USER_DB}")
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}