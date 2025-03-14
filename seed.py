# seed.py

from lib.db.database import SessionLocal, engine
from lib.models.base import Base
from lib.models.book import Book, Author
from lib.models.member import Member
from lib.models.librarian import Librarian
from lib.models.borrow_record import BorrowRecord

# Create all tables if they don't exist
Base.metadata.create_all(engine)

session = SessionLocal()

# Optionally, clear existing data for a fresh seed (useful during development)
session.query(BorrowRecord).delete()
session.query(Book).delete()
session.query(Author).delete()
session.query(Member).delete()
session.query(Librarian).delete()
session.commit()

# Create initial librarians
librarian1 = Librarian(name="John Smith", employee_id="EMP101", email="john.smith@example.com")
librarian2 = Librarian(name="Jane Doe", employee_id="EMP102", email="jane.doe@example.com")
session.add_all([librarian1, librarian2])
session.commit()

# Create initial authors
author1 = Author(name="J.R.R. Tolkien")
author2 = Author(name="George Orwell")
session.add_all([author1, author2])
session.commit()

# Create initial books (each book must have an author and a librarian)
book1 = Book(title="The Hobbit", author_id=author1.id, genre="Fantasy", copies_available=5, librarian_id=librarian1.id)
book2 = Book(title="1984", author_id=author2.id, genre="Dystopian", copies_available=3, librarian_id=librarian2.id)
session.add_all([book1, book2])
session.commit()

# Create initial members
member1 = Member(name="Alice Brown", email="alice.brown@example.com")
member2 = Member(name="Bob Green", email="bob.green@example.com")
session.add_all([member1, member2])
session.commit()

# Optionally, create an initial borrow record to simulate a book being borrowed
borrow1 = BorrowRecord(book_id=book1.id, member_id=member1.id, librarian_id=librarian1.id)
session.add(borrow1)
# Adjust available copies for the borrowed book
book1.copies_available -= 1
session.commit()

print("Database seeded successfully!")
session.close()
