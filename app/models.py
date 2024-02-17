from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from employee import Employee
from factory import Factory
from manager import Manager
from shift import Shift

from shift import Shift
from datetime import datetime

# Create an engine and bind it to a session
engine = create_engine('sqlite:///factory_data.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Create instances of models
factory = Factory(location="Example Location", type="Example Type")
manager = Manager(first_name="John", last_name="Doe", gender="Male", joined_date=datetime.now(), email="john@example.com", employee_no="12345", salary_type="Monthly", salary_amount=5000, job_title="Manager", role="Admin")
employee = Employee(first_name="Jane", last_name="Smith", gender="Female", joined_date=datetime.now(), email="jane@example.com", employee_no="67890", salary_type="Hourly", salary_amount=15, job_title="Worker", role="Worker")
shift = Shift(shift_name="Morning", shift_supervisor="Supervisor")

# Associate objects
factory.managers.append(manager)
factory.employees.append(employee)
shift.manager = manager
shift.employees.append(employee)

# Add instances to the session
session.add(factory)
session.add(manager)
session.add(employee)
session.add(shift)

# Commit changes
session.commit()

# Query data
# Example: Retrieve all factories
factories = session.query(Factory).all()
for factory in factories:
    print(f"Factory ID: {factory.id}, Location: {factory.location}, Type: {factory.type}")

# Example: Retrieve all managers
managers = session.query(Manager).all()
for manager in managers:
    print(f"Manager ID: {manager.id}, Name: {manager.first_name} {manager.last_name}, Email: {manager.email}")

# Example: Retrieve all employees
employees = session.query(Employee).all()
for employee in employees:
    print(f"Employee ID: {employee.id}, Name: {employee.first_name} {employee.last_name}, Email: {employee.email}")

# Example: Retrieve all shifts
shifts = session.query(Shift).all()
for shift in shifts:
    print(f"Shift ID: {shift.id}, Name: {shift.shift_name}, Supervisor: {shift.shift_supervisor}")
