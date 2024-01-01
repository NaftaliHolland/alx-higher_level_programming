#!/usr/bin/python3
""" Script that prints the first state object from a database """

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                    user_name,
                    password,
                    db_name
                )
        )

    # create a session class
    Session = sessionmaker(bind=engine)

    # create the tables from classes
    Base.metadata.create_all(engine)

    # create a session object
    session = Session()

    # send query
    first_state = session.query(State) \
        .order_by(State.id.asc()) \
        .first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
