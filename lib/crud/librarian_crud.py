from lib.models.librarian import Librarian
from lib.db.database import SessionLocal

def create_librarian(name, employee_id, email):
    session = SessionLocal()
    new_librarian = Librarian(name=name, employee_id=employee_id, email=email)
    session.add(new_librarian)
    session.commit()
    session.close()
    return new_librarian

def get_all_librarians():
    session = SessionLocal()
    librarians = session.query(Librarian).all()
    session.close()
    return librarians

def get_librarian_by_id(librarian_id):
    session = SessionLocal()
    librarian = session.query(Librarian).filter_by(id=librarian_id).first()
    session.close()
    return librarian

def update_librarian(librarian_id, **kwargs):
    session = SessionLocal()
    librarian = session.query(Librarian).filter_by(id=librarian_id).first()
    if librarian:
        for key, value in kwargs.items():
            setattr(librarian, key, value)
        session.commit()
    session.close()
    return librarian

def delete_librarian(librarian_id):
    session = SessionLocal()
    librarian = session.query(Librarian).filter_by(id=librarian_id).first()
    if librarian:
        session.delete(librarian)
        session.commit()
    session.close()
    return librarian
