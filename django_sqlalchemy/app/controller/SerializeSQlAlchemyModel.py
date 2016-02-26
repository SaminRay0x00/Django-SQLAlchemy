from json import dumps
from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.session import sessionmaker
from db.ConnectorDB import ConnectMySQL
from app.model.UserModel import django_sqlA


class serialize_sqlalchemy(object):

	    def serialize(self,model):

	        self.columns = [c.key for c in class_mapper(model.__class__).columns]
    	        return dict((c, getattr(model, c)) for c in self.columns)


	    def SelectAll(self):

                        Session = sessionmaker(bind=ConnectMySQL())
                        self.sessiondb = Session()
                        self.serialized_labels = [serialize_sqlalchemy().serialize(label) for label in self.sessiondb.query(django_sqlA).all()]
                        self.my_json = dumps(self.serialized_labels)
                        return self.my_json
