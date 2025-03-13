from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .base import Base

class BorrowRecord(Base):
    __tablename__ = 'borrow_records'

    # Columns
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)  # It links to Book
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)  # It links to Member
    librarian_id = Column(Integer, ForeignKey('librarians.id'), nullable=False)  # It links to Librarian who issued the book
    borrow_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Defaults to current timestamp
    return_date = Column(DateTime, nullable=True, onupdate=lambda: datetime.now(timezone.utc))# Nullable, set when book is returned

    # Relationships
    book = relationship("Book", back_populates="borrow_records")  # Many-to-One: A borrow record belongs to one book
    member = relationship("Member", back_populates="borrow_records")  # Many-to-One: A borrow record belongs to one member
    librarian = relationship("Librarian", back_populates="borrow_records")  # Many-to-One: A borrow record belongs to one librarian

