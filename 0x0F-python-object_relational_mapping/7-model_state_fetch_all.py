#!/usr/bin/python3
""" Lists all State objects from a database using SQLAlchemy """

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

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    states = session.query(State) \
        .order_by(State.id.asc()) \
        .all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
