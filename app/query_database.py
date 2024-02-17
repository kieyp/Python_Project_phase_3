from sqlalchemy.orm import sessionmaker
from model import engine, Factory,Employee,Manager,Shift  # Assuming Factory is one of your database models

from model import Base, engine, Session

# Define a function to retrieve all data from the database
def retrieve_all_data():
    session = Session()

    # Query all records from each table and store the results in variables
    factories = session.query(Factory).all()
    managers = session.query(Manager).all()
    employees = session.query(Employee).all()
    shifts = session.query(Shift).all()

    # Close the session
    session.close()

    # Return the retrieved data
    return {
        "factories": factories,
        "managers": managers,
        "employees": employees,
        "shifts": shifts
    }

# Call the function to retrieve all data
all_data = retrieve_all_data()

# Print or process the retrieved data as needed
print("Factories:", all_data["factories"])
print("Managers:", all_data["managers"])
print("Employees:", all_data["employees"])
print("Shifts:", all_data["shifts"])
