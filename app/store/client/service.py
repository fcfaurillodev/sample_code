from app.store.client.model.client import Client
from app.db.mysql import db

"""
Mysql DB operations for client object
"""

def get_client(client_id):
    return db.session.query(Client).filter(Client.client_id==client_id).first()