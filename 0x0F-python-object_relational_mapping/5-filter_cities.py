#!/usr/bin/python3
""" a script that takes in the name of a state as an argument
and lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == '__main__':
    """Prevent script from working when function is imported"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    # create cursor
    cur = db.cursor()

    # define SQL quer\y
    query = """SELECT cities.name \
            FROM cities \
            INNER JOIN states \
            ON states.id=cities.state_id \
            WHERE states.name=%s \
            ORDER BY cities.id ASC"""

    # execute query
    cur.execute(query, (state_name, ))

    cities = cur.fetchall()

    # print results
    for city in cities:
        print(city)

    # close all connections/clean-up
    cur.close()
    db.close()
