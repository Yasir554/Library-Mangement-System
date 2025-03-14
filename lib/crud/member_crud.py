from lib.models.member import Member
from lib.models.borrow_record import BorrowRecord
from lib.db.database import SessionLocal

def create_member(name, email):
    session = SessionLocal()
    new_member = Member(name=name, email=email)
    session.add(new_member)
    session.commit()
    session.close()
    return new_member

def get_all_members():
    session = SessionLocal()
    members = session.query(Member).all()
    session.close()
    return members

def find_member_by_id(member_id):
    session = SessionLocal()
    member = session.query(Member).filter_by(id=member_id).first()
    session.close()
    return member

def update_member(member_id, **kwargs):
    session = SessionLocal()
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        for key, value in kwargs.items():
            setattr(member, key, value)
        session.commit()
    session.close()
    return member

def delete_member(member_id):
    session = SessionLocal()
    # Delete associated borrow records first to avoid orphans
    session.query(BorrowRecord).filter_by(member_id=member_id).delete()
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        session.delete(member)
        session.commit()
    session.close()
    return member
