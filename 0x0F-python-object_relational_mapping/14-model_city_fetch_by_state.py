#!/usr/bin/python3
"""
Script to Add State record of database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    states = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
