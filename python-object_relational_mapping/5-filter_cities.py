#!/usr/bin/python3
"""The purpose of this module is to run MySQLdb"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    query = "SELECT cities.name FROM cities " \
            "JOIN states " \
            "ON cities.state_id = states.id " \
            "WHERE states.name LIKE %s" \
            "ORDER BY cities.id ASC"

    cur.execute(query, (sys.argv[4],))

    cities = []
    row = cur.fetchone()
    while row:
        cities.append(row[0])
        row = cur.fetchone()
    cities = ", ".join(cities)
    print(cities)

