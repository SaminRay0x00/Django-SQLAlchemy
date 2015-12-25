import sqlalchemy
from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker



def ConnectEngine():

        engine = create_engine('mysql://root:@localhost/tutorial-ramin', echo=True)
        return engine


class ConnectorPostgres():

    def connect(self):
        self.engine = create_engine('postgresql://scott:tiger@localhost/mydatabase', echo=True)
        Session = sessionmaker(bind=self.engine)
        session = Session()



class ConnectorOracle():

    def connect(self):
        self.engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname', echo=True)
        Session = sessionmaker(bind=self.engine)
        session = Session()



class ConnectorSQLite():

    def connect(self):
        self.engine = create_engine('sqlite:////absolute/path/to/foo.db', echo=True)
        Session = sessionmaker(bind=self.engine)
        session = Session()
