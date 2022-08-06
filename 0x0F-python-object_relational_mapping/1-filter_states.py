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
    con = MySQLdb.connect(host="localhost",
                          user=usr,
                          port=3306,
                          passwd=pwd, db=db)
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'
                ORDER BY states.id ASC")
    records = cur.fetchall()
    for row in records:
        print(row)

    cur.close()
    con.close()
