import ipdb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
from model import Factory, Manager, Employee, Shift  # Import your SQLAlchemy models

# Create an engine
engine = create_engine('sqlite:///factory_data.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker instance
faker = Faker()

# Generate fake data for Factory
factory_data = [{'location': faker.city(), 'type': faker.word()} for _ in range(10)]
factories = [Factory(**data) for data in factory_data]

# Generate fake data for Manager
manager_data = [{'first_name': faker.first_name(), 'last_name': faker.last_name(),
                 'gender': faker.random_element(elements=('Male', 'Female')),
                 'email': faker.email(), 'employee_no': faker.random_number(digits=4),
                 'salary_type': faker.random_element(elements=('Hourly', 'Monthly')),
                 'salary_amount': faker.random_number(digits=5),
                 'job_title': faker.job(), 'role': faker.random_element(elements=('Supervisor', 'Manager'))}
                for _ in range(10)]
managers = [Manager(**data) for data in manager_data]

# Generate fake data for Employee
employee_data = [{'first_name': faker.first_name(), 'last_name': faker.last_name(),
                  'gender': faker.random_element(elements=('Male', 'Female')),
                  'Joined_date': faker.date_time_between(start_date='-5y', end_date='now'),
                  'email': faker.email(), 'employee_no': faker.random_number(digits=4),
                  'salary_type': faker.random_element(elements=('Hourly', 'Monthly')),
                  'salary_amount': faker.random_number(digits=5),
                  'job_title': faker.job(), 'role': faker.random_element(elements=('Worker', 'Staff'))}
                 for _ in range(20)]
employees = [Employee(**data) for data in employee_data]

# Generate fake data for Shift
shift_data = [{'shift_name': faker.word(), 'shift_supervisor': faker.name()}
              for _ in range(5)]
shifts = [Shift(**data) for data in shift_data]

# Add generated data to the session
session.add_all(factories)
session.add_all(managers)
session.add_all(employees)
session.add_all(shifts)

# Commit the session to persist changes to the database
session.commit()

# Set a breakpoint
ipdb.set_trace()

# Now you can interactively test your data using ipdb
# For example, you can query the database to check if data is inserted correctly
factories = session.query(Factory).all()
print(factories)

managers = session.query(Manager).all()
print(managers)

employees = session.query(Employee).all()
print(employees)

shifts = session.query(Shift).all()
print(shifts)

# Remember to close the session when you're done
session.close()
