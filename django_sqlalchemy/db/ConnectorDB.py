from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.dbconfig import MySQLInfo
from config.dbconfig import OracleInfo
from config.dbconfig import PostgresInfo

def ConnectMySQL():

    try:
        con = 'mysql://{}:{}@{}:{}/{}?charset=utf-8'.format(MySQLInfo().USERNAME,MySQLInfo().PASSWORD,MySQLInfo().IPADDRESSDATABASE,MySQLInfo().MySQLInfo().PORT,MySQLInfo().DBNAME)
        engine = create_engine(con, echo=True)
        return engine

    except Exception as e:
        raise e


class ConnectorPostgres():

    try:
        def connect(self):
            self.con = 'postgresql://{}:{}@{}:{}/{}?charset=utf-8'.format(PostgresInfo().USERNAME,PostgresInfo().PASSWORD,PostgresInfo().IPADDRESSDATABASE,PostgresInfo().PostgresInfo().PORT,PostgresInfo().DBNAME)
            self.engine = create_engine(self.con, echo=True)
            return self.engine
    except Exception as e:

        raise e


class ConnectorOracle():

    def connect(self):
        self.engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname?charset=utf-8', echo=True)
        Session = sessionmaker(bind=self.engine)
        session = Session()



class ConnectorSQLite():

    def connect(self):
        self.engine = create_engine('sqlite:////absolute/path/to/foo.db?charset=utf-8', echo=True)
        Session = sessionmaker(bind=self.engine)
        session = Session()
