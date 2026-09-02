from fastapi import FastAPI
from pydantic import BaseModel
from db import db as db_router
from auth_login import auth_login

app = FastAPI()

app.include_router(db_router)
app.include_router(auth_login)

@app.get("/")
def read_root():
    return {"Hello": "World"}

class NewBook(BaseModel):
    title: str
    author: str

books = []

@app.post("/books")
def create_book(book: NewBook):
    books.append(book)
    return {"title": book.title, "author": book.author}
