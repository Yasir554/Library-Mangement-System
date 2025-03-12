from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.base import Base

DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

