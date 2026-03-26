from database import LibraryDB
from enums import Genre, Status
from models import Book
from fastapi import FastAPI, HTTPException

db = LibraryDB()
app = FastAPI()

@app.post("/books")
def add_book(book: Book):
    return db.add_book(book)

@app.get("/books")
def list_books():
    return db.list_books()

