from django.db.models.fields.related import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from config.dbconfig import CONNECTOR


Base = declarative_base()



class django_sqlA(Base):

        __tablename__ = 'sqlalchemy_django'

        id = Column(Integer, primary_key=True)
        name = Column(String(50))
        fullname = Column(String(50))
        password = Column(String(50))

if CONNECTOR:

    from db.ConnectorDB import ConnectMySQL
    Base.metadata.create_all(ConnectMySQL().engine)




'''
# OneToMany
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))

#ManyToOne

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", back_populates="parents")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parents = relationship("Parent", back_populates="child")


#OneToOne

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child = relationship("Child", uselist=False, back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Child", back_populates="child")

'''


