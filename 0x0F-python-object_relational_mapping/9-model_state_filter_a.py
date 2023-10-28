#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa that contain the letter a.
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create an engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create the ORM "handle" - Session
    Session = sessionmaker()
    # Connect engine to Session
    Session.configure(bind=engine)
    # Instantiate a session
    session = Session()

    for state in session.query(State).order_by(State.id):
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
