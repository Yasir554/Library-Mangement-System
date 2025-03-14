from lib.models.book import Book
from lib.db.database import SessionLocal

def create_book(title, author_id, genre, copies_available, librarian_id): # Create a new Book record.
    session = SessionLocal()
    new_book = Book(
        title=title,
        author_id=author_id,
        genre=genre,
        copies_available=copies_available,
        librarian_id=librarian_id
    )
    session.add(new_book)
    session.commit()
    session.close()
    return new_book

def get_all_books(): # Retrieve all Book records from the database.
    session = SessionLocal()
    books = session.query(Book).all()
    session.close()
    return books

def find_book_by_id(book_id): # Find a Book record by its ID.
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()
    session.close()
    return book

def update_book(book_id, **kwargs): # Update a Book record.
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        for key, value in kwargs.items():
            setattr(book, key, value)
        session.commit()
    session.close()
    return book

def delete_book(book_id): # Delete a Book record by its ID.
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
    session.close()
    return book

