from library_system import Library

def main():
    library = Library()

    while True:
        print("\n--- Digital Library System ---")
        print("1. Add a Book")
        print("2. View Available Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. View Borrowed Books")
        print("6. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            user_name = input("Enter your name: ")
            book_id = int(input("Enter book ID to borrow: "))
            library.borrow_book(book_id, user_name)

        elif choice == "4":
            user_name = input("Enter your name: ")
            book_id = int(input("Enter book ID to return: "))
            library.return_book(book_id, user_name)

        elif choice == "5":
            library.view_borrowed_books()

        elif choice == "6":
            print("Thank you for using the Digital Library System. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
