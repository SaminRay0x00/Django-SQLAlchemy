from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, Binary



### Define Image for store DB (BLOB)

Base = declarative_base()

class Image(Base):

        __tablename__ = 'img'
        ID = Column(Integer, primary_key=True)
        image = Column(Binary(1000000)) #default size 64KB Now 314KB defined


from config.dbconfig import CONNECTOR
if CONNECTOR:
        from db.ConnectorDB import ConnectMySQL
        Base.metadata.create_all(ConnectMySQL().engine)
