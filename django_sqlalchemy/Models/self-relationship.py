from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.orm import relationships
from sqlalchemy.orm import relationship
Base = declarative_base()



class Student(Base):

        __tablename__ = 'reltest'

        id = Column(Integer, primary_key=True)
        name = Column(String(50))
        fullname = Column(String(50))
        password = Column(String(50))
        parent_id = Column(Integer, ForeignKey('reltest.id'))
        children = relationship(lambda: Student, remote_side=[id])

from Models.ConnectorDB import ConnectEngine
Base.metadata.create_all(ConnectEngine().engine)
