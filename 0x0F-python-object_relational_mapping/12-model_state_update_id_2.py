#!/usr/bin/python3
"""
Lists the first State object from the database
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    sql = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password,
                                                      database)
    engine = create_engine(sql, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state_2 = session.query(State).filter(State.id == 2).first()
    state_2.name = 'New Mexico'
    session.commit()
