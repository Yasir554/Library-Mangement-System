# Library Management System

## Project Description

The Library Management System is a Python-based CLI application designed to efficiently manage books, members, and borrowing activities. It utilizes SQLAlchemy ORM with SQLite to store and manipulate data while following OOP best practices.

The system enables librarians to add, update, delete, and track books 📚. Members can register, borrow, and return books, ensuring a well-maintained lending system 🔄. Borrow records are maintained for tracking history and overdue returns.

Core Features:
✔ Book Management – Add, search, update, and delete books.
✔ Member Management – Register, search, and delete members.
✔ Borrow & Return System – Track borrowed books with timestamps.
✔ Librarian Control – Secure access for overseeing the library.
✔ Data Validation – Ensures accuracy and prevents inconsistencies.

This CLI-based application provides a structured, user-friendly, and efficient way to manage a library without requiring a graphical interface. 🚀

## The Library Management System consists of four models

### 1️Book Model (models/book.py)

Represents books in the library.
Attributes:
    id (Integer, Primary Key)
    title (String, required)
    author (String, required)
    genre (String, required)
    copies_available (Integer, default 1)
    Relationships:One-to-Many: A book can have multiple BorrowRecords.

### 2️ Member Model (models/member.py)

Represents library members who borrow books.
Attributes:
    id (Integer, Primary Key)
    name (String, required)
    email (String, required, unique)
    Relationships:One-to-Many: A member can have multiple BorrowRecords.

### 3️BorrowRecord Model (models/borrow_record.py)

Tracks the borrowing history of books by members.
Attributes:
    id (Integer, Primary Key)
    book_id (Foreign Key → Book.id)
    member_id (Foreign Key → Member.id)
    borrow_date (DateTime, default current timestamp)
    return_date (DateTime, nullable, initially None)
    Relationships:
        Many-to-One: Linked to a Book.
        Many-to-One: Linked to a Member.

### 4️Librarian Model (models/librarian.py)

Represents librarians who manage book entries and borrowing records.
Attributes:
    id (Integer, Primary Key)
    name (String, required)
    employee_id (String, required, unique)
    email (String, required, unique)
    Relationships:
        One-to-Many: A librarian can add multiple Books.
        One-to-Many: A librarian can oversee multiple BorrowRecords.
