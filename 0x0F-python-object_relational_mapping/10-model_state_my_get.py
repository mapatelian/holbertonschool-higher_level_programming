#!/usr/bin/python3
"""
Lists the first State object from the hbtn_0e_6_usa database
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(
            State.name.like(argv[4])).order_by(State.id).first()
    if not state:
        print("Not found")
    else:
        print(state.id)
    session.close()
