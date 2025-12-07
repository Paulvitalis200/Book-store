from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

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


class UserSchema(BaseModel):
    username: str
    email: str

class BookSchema(BaseModel):
    title: str
    quantity: int

users = []
books = []

@app.post("/create_user")
async def create_user(user_data: UserSchema):
    new_user = {
        "username": user_data.username,
        "email": user_data.email
    }

    users.append(new_user)

    return {
        "message": "User Created Successfully",
        "user": new_user
    }

@app.get("/users")
async def get_users():
    return {
        "message": "Users returned successfully",
        "users": users
    }

@app.post("/create_book")
async def create_book(book_data: BookSchema):
    book = {
        "title": book_data.title,
        "quantity": book_data.quantity
    }

    books.append(book)

    return {
        "message": "Book Added successfully",
        "book": book
    }


@app.get("/books")
async def get_books():
    return {
        "message": "Books retrieved",
        "books": books
    }