from fastapi import FastAPI, HTTPException
from models import Book
from enums import Genre, Status
from database import LibraryDB

app = FastAPI()
db = LibraryDB()

@app.post("/books")
def add_book(book: Book):
    return db.add_book(book)

@app.get("/books")
def list_books():
    return db.list_books()

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = db.get_book(book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: Book):
    updated = db.update_book(book_id, book_data)
    if not updated:
        raise HTTPException(404, "Book not found")
    return updated

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    success = db.delete_book(book_id)
    if not success:
        raise HTTPException(404, "Book not found")
    return {"message": "Book deleted"}

@app.get("/books/filter")
def filter_books(genre: Genre | None = None, status: Status | None = None):
    books = db.list_books()
    if genre:
        books = [b for b in books if b.genre == genre]
    if status:
        books = [b for b in books if b.status == status]
    return books


