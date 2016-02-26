from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from app.model.UserModel import Base
from app.model.UserModel import django_sqlA
from db.ConnectorDB import ConnectMySQL


def InsertDB(pmodel):

       Session = sessionmaker(bind=ConnectMySQL())
       sessiondb = Session()
       users   =  pmodel
       sessiondb.add(users)
       sessiondb.commit()
       sessiondb.close()


def Delete(pModel=django_sqlA(),pID=5):

       Session = sessionmaker(bind=ConnectMySQL())
       sessiondb = Session()
       q = text("DELETE FROM :model12 WHERE id=:pidd")
       our_user = sessiondb.execute(q,{'model12':pModel.__tablename__,'pidd':pID})
       sessiondb.commit()
       sessiondb.close()


def SelectAll(student):

       Session = sessionmaker(bind=ConnectMySQL())
       sessiondb = Session()
       lst =  sessiondb.query(student).all()
       return lst

def Edit(pModel):

       Session = sessionmaker(bind=ConnectMySQL())
       sessiondb = Session()
       editusers   =  pModel
       sessiondb.merge(editusers)
       sessiondb.commit()
       sessiondb.close()

def Transaction():

    Session = sessionmaker(bind=ConnectMySQL(),autocommit=True)
    sessiondb = Session()
    trans = sessiondb.begin()
    try:
         ed_user   =  django_sqlA(name="ramin",fullname="fara",password=1234345)
         sessiondb.add(ed_user)
         df = django_sqlA(name="love",fullnam1e="hehehooo",password=1234345)
         sessiondb.add(df)
         trans.commit()

    except:
        trans.rollback()
        raise


def SelectOne():
      pass
