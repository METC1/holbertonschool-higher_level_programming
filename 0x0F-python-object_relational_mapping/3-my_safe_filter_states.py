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
    N = argv[4]
    con = MySQLdb.connect(host="localhost",
                          user=usr,
                          port=3306,
                          passwd=pwd, db=db)
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY states.name\
                LIKE BINARY %s ORDER BY states.id ASC", [N])
    records = cur.fetchall()
    for row in records:
        print(row)

    cur.close()
    con.close()
