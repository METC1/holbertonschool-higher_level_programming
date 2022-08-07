#!/usr/bin/python3
"""
Script to connect and list all states from the hbtn_0e_0_usa database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    state = argv[4]
    con = MySQLdb.connect(host="localhost",
                          user=usr,
                          port=3306,
                          passwd=pwd, db=db)
    cur = con.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN\
                states ON states.id = cities.state_id WHERE\
                states.name = %s ORDER BY cities.id ASC", [state])
    records = cur.fetchall()
    separator = 0
    for row in records:
        if separator != 0:
            print(", ", end="")
        print(row[0], end="")
        separator = 1
    print()
    cur.close()
    con.close()
