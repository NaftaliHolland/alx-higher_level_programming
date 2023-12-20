#!/usr/bin/python3
""" Lists all states from the database """
if __name__ == "__main__":
    import sys
    import MySQLdb

    user_name = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Make connection
    db_conn = MySQLdb.connect(
                host="localhost",
                port=3306, user=user_name,
                passwd=pwd,
                db=db_name,
                charset="utf8"
            )
    # Create cursor
    curs = db_conn.cursor()
    curs.execute("""SELECT * FROM states ORDER BY id ASC""")
    all_states = curs.fetchall()
    for state in all_states:
        print(state)

    # close cursor and connection
    curs.close()
    db_conn.close()
