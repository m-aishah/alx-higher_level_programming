#!/usr/bin/python3
"""Changes the name of a State object in the database hbtn_0e_6_usa."""

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

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
