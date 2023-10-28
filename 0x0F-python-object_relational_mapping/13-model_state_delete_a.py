#!/usr/bin/python3
"""
Deletes all State objects from the database hbtn_0e_6_usa,
                                                    that contain the letter a.
"""

import sys
from model_state import State
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

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()
