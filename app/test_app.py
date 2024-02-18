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
    generated_emails = set()  # Keep track of generated email addresses

    # Generate 1000 records of all kinds of relationships
    for _ in range(1000):
        # Generate random data for a factory
        factory_data = {
            "location": faker.city(),
            "type": faker.word()
        }
        factory = Factory(**factory_data)
        db.add(factory)

        # Generate random data for a manager
        manager_data = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "gender": faker.random_element(elements=("Male", "Female")),
            "email": None,
            "employee_no": faker.random_number(digits=3),  # Disable unique tracking
            "salary_type": faker.random_element(elements=("Hourly", "Monthly")),
            "salary_amount": faker.random_number(digits=4),
            "job_title": faker.job(),
            "role": "Manager"
        }
        manager_data["email"] = generate_unique_email(faker, generated_emails)
        manager = Manager(**manager_data)
        factory.managers.append(manager)

        # Generate random data for employees
        employees_data = [{
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "gender": faker.random_element(elements=("Male", "Female")),
            "email": None,
            "employee_no": faker.random_number(digits=3),  # Disable unique tracking
            "salary_type": faker.random_element(elements=("Hourly", "Monthly")),
            "salary_amount": faker.random_number(digits=4),
            "job_title": faker.job(),
            "role": "Production"
        } for _ in range(2)]  # Generate 2 employees
        for data in employees_data:
            data["email"] = generate_unique_email(faker, generated_emails)
        employees = [Employee(**data) for data in employees_data]
        factory.employees.extend(employees)

        # Generate random data for a shift
        shift_data = {
            "shift_name": faker.word(),
            "shift_supervisor": f"{manager_data['first_name']} {manager_data['last_name']}"
        }
        shift = Shift(**shift_data)
        factory.shifts.append(shift)

        # Add employees to shift
        for employee in employees:
            employee.shifts.append(shift)

    # Commit all changes
    db.commit()

def generate_unique_email(faker, generated_emails):
    email = faker.email()
    while email in generated_emails:
        email = faker.email()
    generated_emails.add(email)
    return email
