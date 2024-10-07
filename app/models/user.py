from app.backend.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from sqlalchemy.schema import CreateTable


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    task = relationship(argument="Task", back_populates="User")

print(CreateTable(User.__table__))
