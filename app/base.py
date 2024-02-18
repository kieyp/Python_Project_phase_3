from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

employee_shift_association = Table(
    "employee_shift_association",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id")),
    Column("shift_id", Integer, ForeignKey("shifts.id"))
)
