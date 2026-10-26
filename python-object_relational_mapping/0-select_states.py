#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost:3036", user=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2])
    cur = db.cursor()

    print(cur.execute("SELECT * FROM states"))
