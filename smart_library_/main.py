# main.py
# Smart Library Manager - a simple library program for beginners.
# Run this file with: python main.py

from books import load_books, add_book, view_books
from search import search_book
from issue_return import issue_book, return_book


def show_menu():
    """Print the main menu."""
    print("\n===== Smart Library Manager =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")


def main():
    """Run the whole program."""
    books = load_books()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            print("Thank you for using Smart Library Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


main()