from lib.models.author import Author
from lib.db.database import SessionLocal

def create_author(name):
    """
    Create a new Author record and return its ID.
    """
    session = SessionLocal()
    new_author = Author(name=name)
    session.add(new_author)
    session.commit()  # Commit so that new_author.id is generated
    author_id = new_author.id  # Capture the ID before closing the session
    session.close()
    return author_id


def get_all_authors():
    """
    Retrieve all Author records.
    """
    session = SessionLocal()
    authors = session.query(Author).all()
    session.close()
    return authors

def find_author_by_id(author_id):
    """
    Retrieve an Author record by its ID.
    """
    session = SessionLocal()
    author = session.query(Author).filter_by(id=author_id).first()
    session.close()
    return author

def find_author_by_name(name):
    """
    Find an Author by name (case-insensitive).
    """
    session = SessionLocal()
    author = session.query(Author).filter(Author.name.ilike(name)).first()
    session.close()
    return author

def update_author(author_id, **kwargs):
    """
    Update an Author record.
    """
    session = SessionLocal()
    author = session.query(Author).filter_by(id=author_id).first()
    if author:
        for key, value in kwargs.items():
            setattr(author, key, value)
        session.commit()
    session.close()
    return author

def delete_author(author_id):
    """
    Delete an Author record.
    (Make sure that there are no books associated with this author before deleting.)
    """
    session = SessionLocal()
    author = session.query(Author).filter_by(id=author_id).first()
    if author and not author.books:
        session.delete(author)
        session.commit()
        session.close()
        return author
    else:
        session.close()
        print("Cannot delete author: there are books associated with this author.")
        return None
