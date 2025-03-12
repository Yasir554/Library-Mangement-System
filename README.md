# 📚 Library Management System  

## 📖 Project Description  

The **Library Management System** is a Python-based **CLI application** designed to efficiently manage books, members, and borrowing activities. It leverages **SQLAlchemy ORM with SQLite** to store and manipulate data while following **OOP best practices**.  

The system enables **librarians** to **add, update, delete, and track books**, while **members** can **register, borrow, and return books**. Borrow records are maintained for tracking history and overdue returns.  

### **🔹 Core Features:**

✔ **Book Management** – Add, search, update, and delete books.  
✔ **Member Management** – Register, search, and delete members.  
✔ **Borrow & Return System** – Track borrowed books with timestamps.  
✔ **Librarian Control** – Secure access for managing books & borrow records.  
✔ **Data Validation** – Ensures accuracy and prevents inconsistencies.  
✔ **Database & Migrations** – Uses **SQLite** with **Alembic** for migrations.  

This **CLI-based application** provides a structured, **user-friendly**, and efficient way to manage a library **without requiring a graphical interface**. 🚀  

---

## **📌 Models Overview**  

The **Library Management System** consists of **four models**:  

### **1️⃣ Book Model (`lib/models/book.py`)**

Represents books in the library.  

- **Attributes:**  
  - `id` (Integer, Primary Key)  
  - `title` (String, required)  
  - `author` (String, required)  
  - `genre` (String, required)  
  - `copies_available` (Integer, default 1)  
  - `librarian_id` (Foreign Key → Librarian.id)  

- **Relationships:**  
  - **One-to-Many:** A book can have multiple **BorrowRecords**.  
  - **Many-to-One:** A book is added by a **Librarian**.  

---

### **2️⃣ Member Model (`lib/models/member.py`)**

Represents library members who borrow books.  

- **Attributes:**  
  - `id` (Integer, Primary Key)  
  - `name` (String, required)  
  - `email` (String, required, unique)  

- **Relationships:**  
  - **One-to-Many:** A member can have multiple **BorrowRecords**.  

---

### **3️⃣ BorrowRecord Model (`lib/models/borrow_record.py`)**  

Tracks borrowing history of books by members.  

- **Attributes:**  
  - `id` (Integer, Primary Key)  
  - `book_id` (Foreign Key → Book.id)  
  - `member_id` (Foreign Key → Member.id)  
  - `borrow_date` (DateTime, default=current timestamp)  
  - `return_date` (DateTime, nullable, initially None)  
  - `librarian_id` (Foreign Key → Librarian.id)  

- **Relationships:**  
  - **Many-to-One:** Linked to a **Book**.  
  - **Many-to-One:** Linked to a **Member**.  
  - **Many-to-One:** Managed by a **Librarian**.  

---

### **4️⃣ Librarian Model (`lib/models/librarian.py`)**

Represents librarians who **manage books and borrowing records**.  

- **Attributes:**  
  - `id` (Integer, Primary Key)  
  - `name` (String, required)  
  - `employee_id` (String, required, unique)  
  - `email` (String, required, unique)  

- **Relationships:**  
  - **One-to-Many:** A librarian can add multiple **Books**.  
  - **One-to-Many:** A librarian can oversee multiple **BorrowRecords**.  

---

## **📌 Librarian Responsibilities**  

Librarians are responsible for managing the library’s operations, including handling books and overseeing borrowing activities.  

### **🔹 Key Responsibilities:**  

✔ **Managing Books** – Adding, updating, and removing books from the library.  
✔ **Overseeing Borrowing** – Approving book borrow requests & tracking returns.  
✔ **Maintaining Records** – Ensuring accurate tracking of book availability.  
✔ **Enforcing Library Policies** – Ensuring correct data entry and preventing duplicates.  

---

### **✅ Final Notes:**  

This Library Management System is designed to be **efficient, scalable, and user-friendly** while ensuring **data integrity** through **validations and relationships**. It is built with **Python, SQLAlchemy, Alembic, and a robust CLI** for seamless interaction.  
