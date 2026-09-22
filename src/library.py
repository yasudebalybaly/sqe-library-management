class Book:
    # Constructor method used to create a new Book object
    def __init__(self, book_id, title, quantity):

        # Check that the book quantity is not negative
        # If the quantity is negative, show an error
        if quantity < 0:
            raise ValueError("Book quantity cannot be negative")

        # Store the unique ID of the book
        self.book_id = book_id

        # Store the title/name of the book
        self.title = title

        # Store the total number of copies of the book
        self.quantity = quantity

        # At the beginning, all copies are available
        self.available = quantity


class Library:
    # Constructor method used to create a new Library object
    def __init__(self):

        # Create an empty dictionary to store books
        # The book ID will be used as the key
        self.books = {}

    def add_book(self, book):
        # Add a book to the library

        # Check if a book with the same ID already exists
        if book.book_id in self.books:

            # Stop the operation and show an error
            raise ValueError("Book ID already exists")

        # Add the book to the dictionary
        # book.book_id is used as the key
        self.books[book.book_id] = book

    def issue_book(self, book_id):
        # Issue one copy of a book to a library user

        # Find the book using its ID
        book = self.books[book_id]

        # Check if there are no available copies
        if book.available <= 0:

            # Stop the operation because the book cannot be issued
            raise ValueError("Book is not available")

        # Reduce the available copies by one
        # because one copy has been issued
        book.available -= 1

        # Return True to show that the book was successfully issued
        return True

    def return_book(self, book_id):
        # Return one copy of a book to the library

        # Find the book using its ID
        book = self.books[book_id]

        # Increase the number of available copies by one
        # because one copy has been returned
        book.available += 1

        # Return True to show that the book was successfully returned
        return True

    def search_book(self, title):
        # Search for a book using its title

        # Go through all books stored in the library
        for book in self.books.values():

            # Check if the current book title matches
            # the title provided by the user
            if book.title == title:

                # Return the matching book
                return book

        # Return None if no book with the given title was found
        return None
