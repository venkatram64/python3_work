from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from my_db.model.base import Base

class ContactDetails(Base):

    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String(20))
    address = Column(String(200))
    actor_Id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship('Actor', backref='contact_details')

    def __init__(self, phone_number, address, actor):
        self.phone_number = phone_number
        self.address = address
        self.actor = actor
