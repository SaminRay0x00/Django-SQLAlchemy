from sqlalchemy.orm import class_mapper
from json import dumps

class serialize_sqlalchemy(object):

	def serialize(self,model):

	    self.columns = [c.key for c in class_mapper(model.__class__).columns]
    	    return dict((c, getattr(model, c)) for c in self.columns)


	def SelectAll(self):

                        Session = sessionmaker(bind=ConnectEngine())
                        self.sessiondb = Session()
                        self.serialized_labels = [serialize(label) for label in sessiondb.query(Student).all()]
                        self.my_json = dumps(self.serialized_labels)

                        return self.my_json
