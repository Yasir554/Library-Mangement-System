from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Author(Base):
    __tablename__ = 'authors'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Relationships
    books = relationship("Book", back_populates="author")  # One-to-Many: An author can write multiple books

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"
