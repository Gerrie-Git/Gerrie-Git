from database import LibraryDB
from enums import Genre, Status
from models import Book

db = LibraryDB()

book_data = Book(
    title="Fantastic Mr Fox",
    author="Roald Dahl",
    genre=Genre.FICTION,
    status=Status.AVAILABLE,
    rating=9
)

db.add_book(book_data)
print(db.list_books())



