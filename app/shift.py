from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base,employee_shift_association
from factory import Factory

class Shift(Base):
    __tablename__ = 'shifts'
    id = Column(Integer(), primary_key=True)
    shift_name = Column(String)
    shift_supervisor = Column(String)

    factory_id = Column(Integer, ForeignKey("factories.id"))
    factory = relationship("Factory", back_populates="shifts")
    employees = relationship("Employee", secondary=employee_shift_association, back_populates="shifts")

    manager_id = Column(Integer, ForeignKey("managers.id"))
    manager = relationship("Manager", back_populates="shifts")
