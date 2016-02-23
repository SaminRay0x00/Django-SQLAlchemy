from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.orm import relationships
from sqlalchemy.orm import relationship


# very important for relationship(Parent/Child)
Base = declarative_base()


class Parent(Base):

    from Models.Child import Child
    __tablename__ = 'parent_test'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

