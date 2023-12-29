#!/usr/bin/python3
""" Connects to a database and excecutes a query """

if __name__ == "__main__":
    import sys
    import MySQLdb

    usr_name = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db_conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                passwd=pwd,
                db=db_name,
                charset="utf8"
            )

    query = """SELECT cities.id, cities.name, states.name FROM cities
                JOIN states ON cities.state_id=states.id
                ORDER BY cities.id"""

    curs = db_conn.cursor()
    curs.execute(query)

    cities_found = curs.fetchall()

    for _ in cities_found:
        print(_)

    curs.close()
    db_conn.close()
