#!/usr/bin/python3
"""Module is for sqlachemy"""

if __name__ == "__main__":
    from model_state import Base, State
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

    try:
        instance = session.query(State).order_by(State.id.asc())[0]
        print(f"{instance.id}: {instance.name}")
    except BaseException:
        print("Nothing")