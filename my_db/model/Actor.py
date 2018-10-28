from sqlalchemy import Column, String, Integer, Date

from my_db.model.base import Base

class Actor(Base):

    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday