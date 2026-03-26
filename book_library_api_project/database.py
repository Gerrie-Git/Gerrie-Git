#In database.py, create a class LibraryDB that:
#Stores books in a list
#Has methods:
#add_book(book)
#get_book(book_id)
#list_books()
#update_book(book_id, book_data)
#delete_book(book_id)
#Use classes, not just functions.

from models import book

class LibraryDB():

    def __init__(self):
        self.books = []

    def add_book(self, books, book):
        books.append(book)
        print(f"{book} has been added to the library")

    

