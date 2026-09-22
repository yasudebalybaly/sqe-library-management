class Book:
    # Class used to store information about a book
    def __init__(self, book_id, title, quantity):
        if quantity < 0:
            raise ValueError("Book quantity cannot be negative")

        self.book_id = book_id
        self.title = title
        self.quantity = quantity
        self.available = quantity


class Library:
    # Class used to manage books in the library
    def __init__(self):
        self.books = {}

    # Method used to add a new book to the library
    def add_book(self, book):
        if book.book_id in self.books:
            raise ValueError("Book ID already exists")

        self.books[book.book_id] = book

    # Method used to issue one copy of a book
    def issue_book(self, book_id):
        book = self.books[book_id]

        if book.available <= 0:
            raise ValueError("Book is not available")

        book.available -= 1

        return True

    # Method used to return one copy of a book
    def return_book(self, book_id):
        book = self.books[book_id]
        book.available += 1

        return True

    # Method used to search for a book by its title
    def search_book(self, title):
        for book in self.books.values():
            if book.title == title:
                return book

        return None
