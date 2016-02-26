from sqlalchemy import Column, Integer, ForeignKey
from app.model.UserModel import Base


class Child(Base):

    __tablename__ = 'child_test'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent_test.id'))

