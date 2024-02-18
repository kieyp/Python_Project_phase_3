from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Factory(Base):
    __tablename__ = 'factories'
    id = Column(Integer, primary_key=True)
    location = Column(String)
    type = Column(String)

    managers = relationship("Manager", back_populates="factory")
    employees = relationship('Employee', back_populates="factory")
    shifts = relationship("Shift", back_populates="factory")
