# sqlalchemy.url = sqlite:///factory_data.db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref
from sqlalchemy import(Column,Table,Integer,String,UniqueConstraint)

engine=create_engine('sqlite:///factory_data.db')

Base=declarative_base()

class Factory(Base):
    __tablename__='factory'
    id=Column(Integer(),primary_key=True)
    location=Column(String())
    type=Column(String())
    

# class Manager():
#     __tablename__='managers'