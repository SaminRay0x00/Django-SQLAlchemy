from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String



Base = declarative_base()



class Student(Base):

        __tablename__ = 'Raminoooooooooo'

        id = Column(Integer, primary_key=True)
        name = Column(String(50))
        fullname = Column(String(50))
        password = Column(String(50))

        '''
        def __repr__(self):
            return "<Student(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

        '''

