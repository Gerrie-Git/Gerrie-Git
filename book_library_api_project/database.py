
from models import Book

class LibraryDB:

    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, book_data):
        book = book_data.copy()
        book.id = self.next_id
        self.next_id += 1
        self.books.append(book)
        return book

    def get_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None
            
    def list_books(self):
        return self.books
    
    def update_book(self, book_id, book_data):
        book = self.books[book_id]
        if not book:
            return None
        
        updated = book.copy(update=book_data.dict(exculde_unset=True))
        self.books = [updated if b.id == book_id else b for b in self.books]
        return updated
    
    
    def delete_book(self, book_id):
        book = self.get_book(book_id)
        if not book:
            return False

        self.books = [b for b in self.books if b.id != book_id]
        return True







