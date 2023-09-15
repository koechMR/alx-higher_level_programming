#!/usr/bin/python3
"""script that takes in an argument and displays values"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
                SELECT
                    cities.name
                FROM
                    cities
                JOIN
                    states
                ON
                    states.id=cities.state_id
                WHERE
                    states.name=%s
                """, (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
