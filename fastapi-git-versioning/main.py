from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

users_db = []


class User(BaseModel):
    name: str
    email: str


@app.post("/users/")
def create_user(user: User):
    users_db.append(user)
    return {"message": "Usuario guardado", "user": user}

@app.get("/users/", response_model=List[User])
def get_users():
    return users_db
