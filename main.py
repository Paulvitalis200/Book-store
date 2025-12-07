from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Hello world!"}

@app.get('/greet/{username}')
async def greet(username:str):
    return {"message": f"Hello {username}"}

@app.get('/name/{newOne}')
async def paul(newOne:str):
    return {"message": f"New {newOne}"}

user_list = [
    "Jerry",
    "Joey",
    "Phil"
]

@app.get('/search')
async def search_for_user(username:str):
    for _ in user_list:
        if username in user_list:
            return {"message": f"details for user {username}"}
        else:
            return {"message": "User Not found"}

@app.get('/hello/')
async def hello(username:Optional[str]="User"):
    return {"message": f"Hello {username}"}