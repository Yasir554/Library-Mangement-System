# 📚 Library Management System

## 📚 Project Description
The Library Management System is a Python-based CLI application designed to efficiently manage library operations. It leverages SQLAlchemy ORM with an SQLite database to store and manipulate data while following object-oriented programming (OOP) best practices. Alembic is used to manage database migrations, and a seed script is provided to populate the database with initial data.

The system ensures that only authorized librarians can manage books and members. Members can borrow and return books, with transactions automatically updating the available copies. Additionally, orphan records are prevented by enforcing relationships among models.

## 🔹 Core Features:
- **Book Management** – Librarians can add, update, and delete books. The system automatically manages author records.
- **Member Management** – Librarians can add and delete members, while members can borrow and return books.
- **Borrow & Return System** – Tracks borrowing history and updates book availability.
- **Librarian Control** – Only authorized librarians can perform administrative tasks.
- **Data Validation & Integrity** – Prevents orphan records and ensures consistency.
- **Database Migrations & Seeding** – Uses Alembic migrations and includes a seed script.

This CLI-based application provides a structured, user-friendly, and efficient way to manage library operations.

## 🖥️ CLI Script Overview
The CLI is implemented in `lib/cli/main.py`, providing a menu-driven interface with the following options:

### Borrow a Book
- Members enter their Member ID and Book ID.
- Librarian verification is required.
- The system decreases the available copies of the book.

### Return a Book
- Members provide the Borrow Record ID.
- The system updates the borrow record and increases available copies.

### List All Books
- Displays books with details such as ID, title, genre, and available copies.

### Manage Books (Librarian Only)
- **Add a Book**: Prompts for book title, author name, genre, and copies.
- **Delete a Book**: Allows deletion by entering the Book ID.

### Manage Members (Librarian Only)
- Librarians can list, add, and delete member records.

### Manage Librarians
- Administrators can list, add, or delete librarians.

### Exit
- Closes the application.

After each operation, users can **return to the main menu** or **exit**.

## ⚙️ Function Overview
### CRUD Operations (Located in `lib/crud/`)
#### Book CRUD (`book_crud.py`)
- `create_book(...)`
- `get_all_books()`
- `find_book_by_id(book_id)`
- `update_book(book_id, **kwargs)`
- `delete_book(book_id)`

#### Member CRUD (`member_crud.py`)
- Functions for creating, listing, finding, updating, and deleting members.

#### Librarian CRUD (`librarian_crud.py`)
- Functions for managing librarians.

#### BorrowRecord CRUD (`borrow_record_crud.py`)
- `create_borrow_record(...)`
- `update_borrow_record(...)`
- Functions for retrieving or deleting borrow records.

#### Author CRUD (`author_crud.py`)
- `find_author_by_name(name)`
- `create_author(name)`
- Functions for managing authors, ensuring books remain linked.

## 🗂️ Models Overview
Defined in `lib/models/`:

### **Author Model (`author.py`)**
- `id`: Primary key.
- `name`: Unique and required.
- **Relationships**: One-to-many with books.

### **Book Model (`book.py`)**
- `id`, `title`, `author_id`, `genre`, `copies_available`, `librarian_id`.
- **Relationships**: Many-to-one with Author & Librarian, One-to-many with BorrowRecords.

### **Member Model (`member.py`)**
- `id`, `name`, `email` (unique).
- **Relationships**: One-to-many with BorrowRecords.

### **BorrowRecord Model (`borrow_record.py`)**
- `id`, `book_id`, `member_id`, `librarian_id`, `borrow_date`, `return_date` (nullable).
- **Relationships**: Many-to-one with Book, Member, and Librarian.

### **Librarian Model (`librarian.py`)**
- `id`, `name`, `employee_id`, `email` (unique).
- **Relationships**: One-to-many with Books & BorrowRecords.

## 🛠️ Database & Migrations
### Database Setup
- `lib/db/database.py` configures SQLite using SQLAlchemy.

### Migrations
- Alembic manages schema changes (`lib/db/`).

### Seed Script
- `seed.py` populates the database with initial data.

## 📝 How to Run the Application
### Set Up the Environment:
```bash
pipenv install
pipenv shell
```

### Run Migrations:
```bash
alembic upgrade head
```

### Seed the Database (Optional):
```bash
python seed.py
```

### Run the CLI:
```bash
python -m lib.cli.main
```
OR
```bash
python lib/cli/main.py
```

## 📚 CLI Script Detailed Explanation
### Main Menu:
- Borrow a Book
- Return a Book
- List All Books
- Manage Books (Librarian Only)
- Manage Members (Librarian Only)
- Manage Librarians
- Exit

### Submenus:
#### Borrow a Book:
- Prompts for Member ID and Book ID.
- Requires librarian verification.
- Reduces available copies.

#### Return a Book:
- Prompts for Borrow Record ID.
- Updates the return date.
- Increases available copies.

#### Manage Books:
- Only accessible to librarians after verification.
- Prompts for title, author, genre, copies when adding.
- Deletes books by Book ID.

#### Manage Members:
- Librarians can list, add, and delete members.

#### Manage Librarians:
- Administrators can list, add, or delete librarians.

### Post-Action Prompt:
After each action, users enter **1 to exit** or **2 to return to the main menu**, ensuring smooth navigation.

