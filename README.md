# Digital Library System

This is a simple command-line Digital Library System where users can view available books, borrow books, return books, and view their borrowed books. The system is designed to simulate a library where users can interact with a collection of books.

## Features

- **Add a Book**: Add new books to the library with a title, author, and unique ID.
- **View Available Books**: Display a list of books that are currently available in the library.
- **Borrow a Book**: Borrow a book from the library if it's available.
- **Return a Book**: Return a book you have borrowed.
- **View Borrowed Books**: View a list of books that are currently borrowed by users.

## Files in the Repository

### 1. `library_system.py`

This file contains the core functionality of the Digital Library System:

- **`Book` class**: Represents a book with attributes such as title, author, and unique ID.
- **`Library` class**: Manages the collection of books and keeps track of borrowed books.
  - **`add_book(title, author)`**: Adds a new book to the library.
  - **`view_books()`**: Displays all available (non-borrowed) books in the library.
  - **`borrow_book(book_id, user_name)`**: Allows a user to borrow a book if it's available.
  - **`return_book(book_id, user_name)`**: Allows a user to return a borrowed book.
  - **`view_borrowed_books()`**: Displays a list of all borrowed books.

### 2. `main.py`

This is the main entry point for the system, where users interact with the library:

- Provides a menu for users to:
  - Add books.
  - View available books.
  - Borrow and return books.
  - View borrowed books.
- The system uses the `Library` class from `library_system.py` to perform the actions.

## How to Run

1. **Install Python**: Ensure that Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Download or clone the repository to your local machine.

3. **Run the system**:
   Open a terminal or command prompt, navigate to the folder containing the files, and run the following command:

   ```bash
   python main.py
