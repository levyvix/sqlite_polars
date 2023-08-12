from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50), unique=True)

    def __repr__(self):
        return "<User(username='%s', password='%s')>" % (
            self.username, self.password)




def populate_database(engine):
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

    # add 1 million rows
    for i in range(1000000):
        user = User(username='user'+str(i), password='password'+str(i))
        session.add(user)

    # commit the record the database
    session.commit()

    # close the session
    session.close()

if __name__ == '__main__':
    #create sqlite database
    engine = create_engine('sqlite:///database.db', echo=False)
    populate_database(engine)
    