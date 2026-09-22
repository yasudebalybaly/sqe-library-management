# sqe-library-management
# Library Management System

## Project Description

The Library Management System is a simple Python project used to manage books in a library. It allows the library to store books, add new books, issue books, return books, and search for books by title.

The project also includes validation to prevent invalid data such as negative book quantities and duplicate book IDs.

## Features

The system provides the following features:

* Add a new book to the library
* Prevent duplicate book IDs
* Check that book quantity is not negative
* Issue an available book
* Return a book
* Search for a book by title
* Track the total and available number of books
* Handle invalid operations using error messages

## Project Structure

```text
library-management/
│
├── src/
│   └── library.py
│
├── tests/
│   └── test_library.py
│
└── README.md
```

## Main Classes

### Book

The `Book` class represents a book in the library.

It stores:

* Book ID
* Book title
* Total quantity
* Available quantity

It also checks that the book quantity is not negative.

### Library

The `Library` class manages the books in the library.

It provides the following methods:

* `add_book()` adds a book to the library
* `issue_book()` issues one available copy
* `return_book()` returns one copy
* `search_book()` searches for a book using its title

## Example

```python
book = Book(1, "Python Basics", 5)

library = Library()

library.add_book(book)

library.issue_book(1)

print(book.available)

library.return_book(1)

print(book.available)
```

## Validation

The project uses validation to handle incorrect input.

For example:

* A negative book quantity is not allowed.
* A duplicate book ID is not allowed.
* A book cannot be issued when no copies are available.

## Testing

The project contains tests to check the main functionality of the system.

The tests can be executed using:

```bash
python -m pytest -v
```

## Purpose

The main purpose of this project is to demonstrate basic software engineering concepts such as object oriented programming, input validation, error handling, testing, and code organization.

## Technologies Used

* Python
* Pytest
* Git
* GitHub

## Author

Muhammad Yasir
