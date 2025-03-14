from lib.models.borrow_record import BorrowRecord
from lib.models.book import Book
from lib.db.database import SessionLocal

def create_borrow_record(book_id, member_id, librarian_id):
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()
    if book and book.copies_available > 0:
        book.copies_available -= 1  # Reduce available copies when borrowed
        new_record = BorrowRecord(
            book_id=book_id,
            member_id=member_id,
            librarian_id=librarian_id
        )
        session.add(new_record)
        session.commit()
        session.close()
        return new_record
    else:
        session.close()
        print("Book not available for borrowing.")
        return None

def update_borrow_record(record_id, **kwargs):
    session = SessionLocal()
    record = session.query(BorrowRecord).filter_by(id=record_id).first()
    if record and not record.return_date:
        for key, value in kwargs.items():
            setattr(record, key, value)
        # If setting return_date, increase available copies
        if 'return_date' in kwargs and kwargs['return_date']:
            book = session.query(Book).filter_by(id=record.book_id).first()
            if book:
                book.copies_available += 1
        session.commit()
    session.close()
    return record

def get_all_borrow_records():
    session = SessionLocal()
    records = session.query(BorrowRecord).all()
    session.close()
    return records

def find_borrow_record_by_id(record_id):
    session = SessionLocal()
    record = session.query(BorrowRecord).filter_by(id=record_id).first()
    session.close()
    return record

def delete_borrow_record(record_id):
    session = SessionLocal()
    record = session.query(BorrowRecord).filter_by(id=record_id).first()
    if record:
        session.delete(record)
        session.commit()
    session.close()
    return record
