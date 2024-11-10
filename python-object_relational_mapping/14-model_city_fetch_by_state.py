#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
