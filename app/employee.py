from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from base import Base, employee_shift_association
from datetime import datetime

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    joined_date = Column(DateTime, default=datetime.now)
    email = Column(String)
    employee_no = Column(String)
    salary_type = Column(String)
    salary_amount = Column(Integer)
    job_title = Column(String)
    role = Column(String)

    factory = relationship('Factory', back_populates="employees")
    factory_id = Column(Integer, ForeignKey('factories.id'))

    shifts = relationship("Shift", secondary=employee_shift_association, back_populates="employees")
