#!/usr/bin/python3
"""
Script to list first State record of database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        usr, pwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).first()
        for state in states:
            print("{}: {}".format(state.id, state.name))
    except:
        print("Nothing")
