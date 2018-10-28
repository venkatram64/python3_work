
from sqlalchemy import Table, ForeignKey, Column, String, Integer, Date
from sqlalchemy.orm import relationship

from my_db.model.base import Base

movies_actor_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    release_date = Column(Date)

    actors = relationship("Actor", secondary=movies_actor_association)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date


