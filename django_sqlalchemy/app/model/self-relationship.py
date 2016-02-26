from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String ,ForeignKey

Base = declarative_base()



class self_reflation(Base):

        __tablename__ = 'reltest'

        id = Column(Integer, primary_key=True)
        name = Column(String(50))
        fullname = Column(String(50))
        password = Column(String(50))
        parent_id = Column(Integer, ForeignKey('reltest.id'))
        children = relationship(lambda: self_reflation, remote_side=[id])

from db.ConnectorDB import ConnectMySQL
Base.metadata.create_all(ConnectMySQL().engine)
