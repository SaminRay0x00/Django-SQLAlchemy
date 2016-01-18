from Models.UserModel import Base
from Models.UserModel import Student
from Models.ConnectorDB import ConnectMySQL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text



def CreateTable():

                Base.metadata.create_all(ConnectMySQL())

def InsertDB(pmodel):

                Session = sessionmaker(bind=ConnectMySQL())
                sessiondb = Session()
                ed_user   =  pmodel
                sessiondb.add(ed_user)
                sessiondb.commit()
                sessiondb.close()


def Delete(pModel=Student(),pID=5):

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
                 ed_user   =  pModel
                 sessiondb.merge(ed_user)
                 sessiondb.commit()
                 sessiondb.close()


def Transaction():

    Session = sessionmaker(bind=ConnectMySQL(),autocommit=True)
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


### EXEC SP 
def exec_procedure(session, proc_name, params):


    sql_params = ",".join(["@{0}={1}".format(name, value) for name, value in params.items()])
    sql_string = """
        DECLARE @return_value int;
        EXEC    @return_value = [dbo].[{proc_name}] {params};
        SELECT 'Return Value' = @return_value;
    """.format(proc_name=proc_name, params=sql_params)

    return session.execute(sql_string).fetchall()


### Call SP 

def call_procedure():



       Session = sessionmaker(bind=ConnectEngine())
       sessiondb = Session()

       params = {
                    'Foo': 1,
                    'Bar': 1   ,
                 }
       exec_procedure(sessiondb, 'MyProc', params)
       
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
