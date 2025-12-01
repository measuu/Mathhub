from sqlalchemy import Column, Float, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    comment = Column(String)
    rating = Column(Float)
