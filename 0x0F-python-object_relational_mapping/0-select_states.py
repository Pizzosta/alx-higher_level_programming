#!/usr/bin/python3
"""This script will create an SQL database and query data from the db"""

import MySQLdb
import sys

if __name__ == '__main__':
    """Prevent script from working when function is imported"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    # create cursor
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()

    # print results
    for state in states:
        print(state)

    # close all connections/clean-up
    cur.close()
    db.close()
