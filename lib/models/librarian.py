from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from .base import Base

class Librarian(Base):
    __tablename__ = 'librarians'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    employee_id = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    # Relationships
    books = relationship("Book", back_populates="librarian", cascade="all, delete-orphan")  # One-to-Many: A librarian adds multiple books
    borrow_records = relationship("BorrowRecord", back_populates="librarian", cascade="all, delete-orphan")  # One-to-Many: A librarian oversees borrowing records
