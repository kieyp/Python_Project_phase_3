import pytest
from faker import Faker
from sqlalchemy.orm import sessionmaker
from model import Factory, Manager, Employee, Shift, engine

@pytest.fixture
def db():
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def faker():
    return Faker()

def test_factory_relationships(db, faker):
    # Create a factory
    factory = Factory(location="New York", type="Electronics")
    db.add(factory)
    db.commit()

    # Create a manager
    manager1 = Manager(first_name="John", last_name="Doe", gender="Male", email=faker.unique.email(), employee_no="001", salary_type="Hourly", salary_amount=20, job_title="Manager", role="Manager")
    factory.managers.append(manager1)

    # Create employees with unique email addresses
    employees = [
        Employee(first_name="Jane", last_name="Smith", gender="Female", email=faker.unique.email(), employee_no="002", salary_type="Hourly", salary_amount=15, job_title="Employee", role="Production"),
        Employee(first_name="Alice", last_name="Johnson", gender="Female", email=faker.unique.email(), employee_no="003", salary_type="Hourly", salary_amount=15, job_title="Employee", role="Production")
    ]
    factory.employees.extend(employees)

    # Create a shift
    shift = Shift(shift_name="Morning", shift_supervisor="John Doe")
    factory.shifts.append(shift)

    # Add employees to shift
    for employee in employees:
        employee.shifts.append(shift)

    # Commit all changes
    db.commit()

    # Query the database
    result = db.query(Factory).filter_by(location="New York").first()

    # Check relationships
    assert result is not None
    assert result.managers[0].first_name == "John"
    assert set(employee.first_name for employee in result.employees) == {"Alice", "Jane"}
    assert result.shifts[0].shift_name == "Morning"
    assert set(employee.first_name for employee in result.shifts[0].employees) == {"Alice", "Jane"}

def test_shift_employees_relationship(db, faker):
    # Create a factory
    factory = Factory(location="New York", type="Electronics")
    db.add(factory)
    db.commit()

    # Create employees
    employee1 = Employee(first_name="Jane", last_name="Smith")
    employee2 = Employee(first_name="Alice", last_name="Johnson")
    db.add_all([employee1, employee2])
    db.commit()

    # Create a shift
    shift = Shift(shift_name="Morning")
    shift.employees.extend([employee1, employee2])
    db.add(shift)
    db.commit()

    # Query the database
    result_shift = db.query(Shift).filter_by(shift_name="Morning").first()

    # Check relationships
    assert result_shift is not None
    assert len(result_shift.employees) == 2
    assert all(employee in result_shift.employees for employee in [employee1, employee2])
    assert employee1 in result_shift.employees
    assert employee2 in result_shift.employees
