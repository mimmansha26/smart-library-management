# Project Statement – Smart Library Manager

## Problem Statement

Managing books in a small library by hand is slow and error-prone. It is hard to keep track of which books are available, which ones have been issued to members, and how to find a book quickly. Smart Library Manager solves this with a simple command-line program that can add books, show all books, search by title, and track issued or returned books using a plain text file.

## Scope

The project covers the basic day-to-day tasks of a small library:

- Storing book information in a local text file (`books.txt`).
- Adding new books to the library.
- Viewing the full list of books with their status.
- Searching for books by title.
- Issuing a book to a member (marking it as not available).
- Returning a book (marking it as available again).

What is **not** included: no database, no graphical interface, no internet features, no member login system, and no user accounts.

## Target Users

- Beginners learning Python who want a small, understandable project.
- Students and hobbyists who want a simple program to practice file handling, menus, loops, and functions.
- Keep it as a sample project for a portfolio or a classroom assignment.

## High-Level Features

- **Menu-driven program** – A simple numbered menu makes it easy to use.
- **Add Book** – Add a new book; the ID is assigned automatically.
- **View Books** – See all books with their status (Available / Issued).
- **Search Book** – Look up books by title; case-insensitive with partial matching.
- **Issue Book** – Mark a book as issued to a member.
- **Return Book** – Mark a book as returned and available again.
- **Persistent storage** – All changes are saved to `books.txt` automatically.