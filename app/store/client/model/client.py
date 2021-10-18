from app.db.mysql import db
from app.db.mysql.serializer import Serializer
from app.utils.json_converter import json_format_converter
import time
import json


class Client(db.Model, Serializer):
    __tablename__ = 'clients'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.String(30), nullable=False, unique=True)
    audience = db.Column(db.String(100), nullable=False, unique=True)
    pub_key = db.Column(db.Text(), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.Numeric(precision=20, scale=7), default=time.time(), nullable=True)
    updated_at = db.Column(db.Numeric(precision=20, scale=7), default=time.time(), nullable=True)

    @classmethod
    def from_dict(cls, _dict: dict):
        """ Converts value from dictionary to Merchant obj """
        p = Client()
        [setattr(p, key, _dict[key]) for key in _dict]
        return p

    @classmethod
    def from_str(cls, entry: str):
        """ Converts value from string to Merchant dictionary """
        _dict = Client.from_str_to_dict(entry)
        return Client.from_dict(_dict)

    @classmethod
    def from_str_to_dict(cls, entry: str) -> dict:
        """ Takes a file-like object and convert that string to create a json object """
        return json.loads(entry)

    def to_dict(self):
        """ Convert Client object into a dictionary """
        if self is None:
            return None
        else:
            # create dictionary with table keys and client object value
            results = {}
            for col in self.__table__.columns.keys():
                obj = getattr(self, col)
                results[col] = json_format_converter(obj)
            return results

    def to_str(self) -> str:
        """ Converts Client object into a string """
        return json.dumps(self.to_dict(), default=json_format_converter)

    def __repr__(self):
        return f"Client(id:'{self.id}', name: '{self.name}' audience: '{self.audience}',"\
               f"pub_key: '{self.pub_key}', active: '{self.active}'), created_at: '{self.created_at}', "\
               f"updated_at: '{self.updated_at}'"