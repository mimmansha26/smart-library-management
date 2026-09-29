
# Smart Library Management System

## Overview

Smart Library Management System is a simple terminal-based Python application designed to manage common library operations. It helps maintain book records, member information, issue/return transactions, and basic library reports.

The project is designed to be easy to run from the command line and suitable for a Python Essentials course project.

## Features

- Add and manage books
- View available books
- Search for books
- Add and manage library members
- Issue books to members
- Return issued books
- Track book availability
- View transactions
- Generate basic library reports
- Input validation and error handling
- Simple command-line interface

## Technology Used

- **Programming Language:** Python 3
- **Interface:** Command Line / Terminal
- **Storage:** Local files
- **External Dependencies:** None, unless specified by the project implementation

## Requirements

- Python 3.x
- VS Code or any terminal/command prompt
- No external database or online service is required for the basic version.

## How to Run

1. Download or clone the project repository.
2. Open the project folder in VS Code or a terminal.
3. Make sure Python 3 is installed.
4. Run the application:

```bash
python main.py
```

## Main Operations

The application provides a terminal menu for common library operations, such as:

1. Add Book
2. View Books
3. Search Book
4. Add Member
5. View Members
6. Issue Book
7. Return Book
8. View Transactions
9. Library Report
10. Exit

The exact menu options may vary depending on the final implementation.

## Data Storage

The system uses local files to store library information. Typical records include:

- Book details
- Member details
- Issue and return transactions
- Book availability

Using local file storage keeps the project simple and avoids requiring an external database or server.

## Validation and Error Handling

The application handles common situations such as:

- Empty input
- Invalid menu choices
- Duplicate book or member records
- Book not found
- Member not found
- Attempting to issue an unavailable book
- Attempting to return a book that was not issued

## Testing

The application can be tested through the terminal by:

- Adding books and members
- Searching for books
- Issuing available books
- Returning issued books
- Trying invalid inputs
- Checking library reports
- Verifying that data is stored correctly

## Project Structure

A typical structure is:

```text
smart_library_management/
│
├── data/
│   ├── books.txt
│   ├── members.txt
│   └── transactions.txt
│
├── main.py
├── books.py
├── members.py
├── transactions.py
├── reports.py
├── database.py
├── validators.py
├── requirements.txt
├── statement.md
├── README.md
└── .gitignore
```

> The exact files may differ depending on the final implementation of the project.

## Limitations

This version is intentionally kept simple for educational purposes.

- Uses local file storage
- No web server is required
- No external database is required
- No graphical user interface
- No cloud synchronization
- No online authentication

## Future Enhancements

Possible future improvements include:

- Graphical user interface
- SQLite/MySQL database integration
- User login and role management
- Automatic fine calculation
- Due-date reminders
- Advanced search and filtering
- Book reservation system
- CSV/PDF report generation
- Web-based library management

## Project Objective

The objective of this project is to apply Python programming concepts to a practical library-management problem while maintaining a simple, modular, and easy-to-understand implementation.

## Author

**Divyansh Chandra**

Python Essentials — Evaluated Course Project
