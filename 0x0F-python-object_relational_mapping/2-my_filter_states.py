#!/usr/bin/python3
""" Takes an argument and displays all values that matche the argument """

if __name__ == "__main__":
    import sys
    import MySQLdb

    user_name = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db_conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                passwd=pwd,
                db=db_name,
                charset="utf8"
            )

    query = """SELECT * FROM states
                WHERE name = '{}'
                ORDER BY id ASC""".format(state_name)
    curs = db_conn.cursor()
    curs.execute(query)

    states_found = curs.fetchall()

    for _ in states_found:
        print(_)

    curs.close()
    db_conn.close()
