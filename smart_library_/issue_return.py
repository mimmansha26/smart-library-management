# issue_return.py
# This file has the functions to issue and return books.

from books import save_books


def issue_book(books):
    """Mark a book as issued (not available) if it is available."""
    try:
        book_id = int(input("Enter book id to issue: "))
    except ValueError:
        print("Please enter a number.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["available"] == "yes":
                book["available"] = "no"
                save_books(books)
                print("Book issued successfully!")
            else:
                print("Sorry, this book is already issued.")
            return

    print("No book found with that id.")


def return_book(books):
    """Mark a book as returned (available again) if it was issued."""
    try:
        book_id = int(input("Enter book id to return: "))
    except ValueError:
        print("Please enter a number.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["available"] == "no":
                book["available"] = "yes"
                save_books(books)
                print("Book returned successfully!")
            else:
                print("This book is not issued.")
            return

    print("No book found with that id.")