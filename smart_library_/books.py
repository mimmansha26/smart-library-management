# books.py
# This file handles loading books, saving books, adding a book, and viewing books.
# Each book is a dictionary: {"id": ..., "title": ..., "author": ..., "available": ...}
# "available" is "yes" if the book is in the library, "no" if it is issued.

FILE_NAME = "books.txt"


def load_books():
    """Read all books from books.txt and return them as a list.
    If the file does not exist, return an empty list."""
    books = []

    try:
        file = open(FILE_NAME, "r")
    except FileNotFoundError:
        print("books.txt not found. Starting with an empty library.")
        return books

    for line in file:
        line = line.strip()          # remove extra spaces and newline
        if line == "":               # skip empty lines
            continue

        parts = line.split("|")      # split the line into 4 parts

        # Each line must have: id | title | author | available
        if len(parts) == 4:
            book = {
                "id": int(parts[0]),
                "title": parts[1],
                "author": parts[2],
                "available": parts[3]
            }
            books.append(book)

    file.close()
    return books


def save_books(books):
    """Write all books to books.txt."""
    file = open(FILE_NAME, "w")

    for book in books:
        line = str(book["id"]) + "|" + book["title"] + "|" + book["author"] + "|" + book["available"]
        file.write(line + "\n")

    file.close()


def add_book(books):
    """Ask the user for a title and author, then add the book as available."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")

    # The new book always gets the next id.
    if len(books) == 0:
        new_id = 1
    else:
        new_id = books[-1]["id"] + 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "available": "yes"
    }

    books.append(book)
    save_books(books)
    print("Book added successfully!")


def view_books(books):
    """Print all books with their availability on the screen."""
    if len(books) == 0:
        print("No books in the library.")
        return

    print("\n--- Books in Library ---")

    for book in books:
        if book["available"] == "yes":
            status = "Available"
        else:
            status = "Issued"

        print(str(book["id"]) + ". " + book["title"] + " by " + book["author"] + " - " + status)

    print("------------------------")