#!/usr/bin/python3
"""Module is for sqlachemy"""

if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    instances = session.query(State, City).\
        filter(City.state_id == State.id).\
        order_by(City.id.asc())

    for state, city in instances:
        print(f"{state.name}: ({city.id}) {city.name}")
