# search.py
# This file has the function to search for books.

def search_book(books):
    """Search for books by title. Partial words also work,
    for example "py" will match "Python Basics"."""
    keyword = input("Enter book title to search: ")
    keyword = keyword.lower()

    found = False
    print("\n--- Search Results ---")

    for book in books:
        title = book["title"].lower()

        if keyword in title:
            if book["available"] == "yes":
                status = "Available"
            else:
                status = "Issued"

            print(str(book["id"]) + ". " + book["title"] + " by " + book["author"] + " - " + status)
            found = True

    if not found:
        print("No book found with that title.")

    print("----------------------")