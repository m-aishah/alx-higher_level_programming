#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_6_usa,
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create an engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create the ORM "handle" - Session
    Session = sessionmaker(bind=engine)
    # Instantiate a session
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):

        print("{}: ({}) {}".format(state.name, city.id, city.name))
