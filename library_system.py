class Book:
    def __init__(self, title, author, book_id):
        """Initialize a book with title, author, and unique ID."""
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False  # Track if the book is borrowed

    def __str__(self):
        """Return a string representation of the book."""
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}"

class Library:
    def __init__(self):
        """Initialize the library with a list of books."""
        self.books = []
        self.borrowed_books = []  # Track borrowed books

    def add_book(self, title, author):
        """Add a new book to the library."""
        book_id = len(self.books) + 1  # Unique ID for each book
        book = Book(title, author, book_id)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def view_books(self):
        """View all available books in the library."""
        if not self.books:
            print("No books available in the library.")
            return
        print("\nAvailable Books:")
        for book in self.books:
            if not book.is_borrowed:
                print(book)

    def borrow_book(self, book_id, user_name):
        """Allow a user to borrow a book if it's available."""
        for book in self.books:
            if book.book_id == book_id and not book.is_borrowed:
                book.is_borrowed = True
                self.borrowed_books.append({'user': user_name, 'book': book})
                print(f"{user_name} successfully borrowed '{book.title}' by {book.author}.")
                return True
        print(f"Sorry, the book with ID {book_id} is not available.")
        return False

    def return_book(self, book_id, user_name):
        """Allow a user to return a borrowed book."""
        for record in self.borrowed_books:
            if record['book'].book_id == book_id and record['user'] == user_name:
                record['book'].is_borrowed = False
                self.borrowed_books.remove(record)
                print(f"{user_name} successfully returned '{record['book'].title}' by {record['book'].author}.")
                return True
        print(f"No borrowed book with ID {book_id} found for {user_name}.")
        return False

    def view_borrowed_books(self):
        """View all books currently borrowed by users."""
        if not self.borrowed_books:
            print("No books are currently borrowed.")
            return
        print("\nBorrowed Books:")
        for record in self.borrowed_books:
            print(f"User: {record['user']}, Book: {record['book'].title} by {record['book'].author}")

