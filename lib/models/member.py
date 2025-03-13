from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Member(Base):
    __tablename__ = "members"

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    # Relationships
    borrow_records = relationship("BorrowRecord", back_populates="member", cascade="all, delete-orphan") # One-to-Many: A member can borrow multiple books
