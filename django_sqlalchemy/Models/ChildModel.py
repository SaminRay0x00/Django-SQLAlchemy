from sqlalchemy import Column, Integer, String ,ForeignKey
from Models.UserModel import Base
from sqlalchemy.orm import relationships
from sqlalchemy.orm import relationship


class Child(Base):
    __tablename__ = 'child_test'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent_test.id'))

