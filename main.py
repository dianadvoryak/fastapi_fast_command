from fastapi import FastAPI
from pydantic import BaseModel
from src.api import main_router

app = FastAPI()

app.include_router(main_router)

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
