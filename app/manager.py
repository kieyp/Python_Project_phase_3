from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from base import Base

class Manager(Base):
    __tablename__ = 'managers'
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

    factory = relationship("Factory", back_populates="managers")
    factory_id = Column(Integer, ForeignKey('factories.id'))

    shifts = relationship("Shift", back_populates="manager")
