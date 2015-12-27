from Models.UserModel import Base
from Models.UserModel import Student
from Models.ConnectorDB import ConnectEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text



def CreateTable():

                Base.metadata.create_all(ConnectEngine())

def InsertDB(pmodel):

                Session = sessionmaker(bind=ConnectEngine())
                sessiondb = Session()
                ed_user   =  pmodel
                sessiondb.add(ed_user)
                sessiondb.commit()
                sessiondb.close()


def Delete(pModel=Student(),pID=5):

               Session = sessionmaker(bind=ConnectEngine())
               sessiondb = Session()
               q = text("DELETE FROM :model12 WHERE id=:pidd")
               our_user = sessiondb.execute(q,{'model12':pModel.__tablename__,'pidd':pID})
               sessiondb.commit()
               sessiondb.close()


def SelectAll(student):

                        Session = sessionmaker(bind=ConnectEngine())
                        sessiondb = Session()
                        lst =  sessiondb.query(student).all()
                        return lst

def Edit(pModel):

                 Session = sessionmaker(bind=ConnectEngine())
                 sessiondb = Session()
                 ed_user   =  pModel
                 sessiondb.merge(ed_user)
                 sessiondb.commit()
                 sessiondb.close()


def Transaction():

    Session = sessionmaker(bind=ConnectEngine(),autocommit=True)
    sessiondb = Session()
    trans = sessiondb.begin()
    try:
         ed_user   =  Student(name="ramin",fullname="fara",password=1234345)
         sessiondb.add(ed_user)
         df = Student(name="love",fullnam1e="hehehooo",password=1234345)
         sessiondb.add(df)
         trans.commit()

    except:
        trans.rollback()
        raise
      
      
def SelectOne():
                pass
              
def SelectOne():
                pass
              
def main():

                #o = Helper()
                #Delete()
                Transaction()
                #Insert()
                #Delete()
                #SelectOne()



if __name__ == "__main__":
                main()
