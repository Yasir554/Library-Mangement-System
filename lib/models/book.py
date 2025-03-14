from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .author import Author

class Book(Base):
    __tablename__ = 'books'

    # Columns
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    genre = Column(String, nullable=False)
    copies_available = Column(Integer, default=1, nullable=False)
    librarian_id = Column(Integer, ForeignKey('librarians.id'), nullable=False)

    # Relationships
    author = relationship("Author", back_populates="books")  # Many-to-One: A book has one author, an author has many books
    librarian = relationship("Librarian", back_populates="books")  # Many-to-One: A book is added by a librarian
    borrow_records = relationship("BorrowRecord", back_populates="book", cascade="all, delete-orphan")  # One-to-Many: A book can have multiple borrow records


