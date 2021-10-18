from app.db.mysql import db
from app.db.mysql.serializer import Serializer
from app.utils.json_converter import json_format_converter
import time
import json


class Merchant(db.Model, Serializer):
    __tablename__ = 'merchants'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    identity_id = db.Column(db.String(100), nullable=False, unique=True)
    merchant_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    contact_person = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Numeric(precision=20, scale=7), default=time.time(), nullable=True)
    updated_at = db.Column(db.Numeric(precision=20, scale=7), default=time.time(), nullable=True)

    @classmethod
    def from_dict(cls, _dict: dict):
        """ Converts value from dictionary to Merchant obj """
        p = Merchant()
        [setattr(p, key, _dict[key]) for key in _dict]
        return p

    @classmethod
    def from_str(cls, entry: str):
        """ Converts value from string to Merchant dictionary """
        _dict = Merchant.from_str_to_dict(entry)
        return Merchant.from_dict(_dict)

    @classmethod
    def from_str_to_dict(cls, entry: str) -> dict:
        """ Takes a file-like object and convert that string to create a json object """
        return json.loads(entry)

    @classmethod
    def from_list(cls, entry_list):
        """ Converts list to Merchant list """
        list = [entry.to_dict() for entry in entry_list]
        return list

    @classmethod
    def to_str_list(cls, entries) -> str:
        """ Takes a json object and returns a string """
        return json.dumps(entries, default=json_format_converter)

    def to_dict(self):
        """ Convert Merchant object into a dictionary """
        if self is None:
            return None
        else:
            # create dictionary with table keys and merchant object value
            results = {}
            for col in self.__table__.columns.keys():
                obj = getattr(self, col)
                results[col] = json_format_converter(obj)
            return results

    def to_str(self) -> str:
        """ Converts Merchant object into a string """
        return json.dumps(self.to_dict(), default=json_format_converter)

    def __repr__(self):
        return f"Merchant(id:'{self.id}', identity_id: '{self.identity_id}', merchant_name: '{self.merchant_name}',"\
               f"description: '{self.description}', contact_person: '{self.contact_person}', contact_number: '{self.contact_number}', "\
               f"contact_email: '{self.contact_email}', address: '{self.address}', created_at: '{self.created_at}', "\
               f"updated_at: '{self.updated_at}')"

