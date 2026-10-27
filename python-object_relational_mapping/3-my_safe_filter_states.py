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
    query = "SELECT * FROM states " \
            "WHERE name LIKE BINARY %s " \
            "ORDER BY id ASC"
    
    cur.execute(query, (sys.argv[4], ))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)


