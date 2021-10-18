from app.store.merchant.model.merchant import Merchant
from app.db.mysql import db
import time

"""
Mysql DB operations for Merchant object
"""

def get_merchant(merchant_id: str) -> Merchant:
    return db.session.query(Merchant).get(merchant_id)


def get_merchant_by_identity(identity_id: str) -> Merchant:
    return db.session.query(Merchant).filter(Merchant.identity_id==identity_id).first()


def create_merchant(merchant: Merchant) -> Merchant:
    db.session.add(merchant)
    db.session.commit()
    return merchant


def update_merchant(merchant_id: str, new_merchant_details: Merchant) -> Merchant:
    merchant_record = Merchant.query.filter_by(id=merchant_id).first()
    if merchant_record:
        if new_merchant_details.merchant_name:
            merchant_record.merchant_name = new_merchant_details.merchant_name
        if new_merchant_details.description:
            merchant_record.description = new_merchant_details.description
        if new_merchant_details.contact_person:
            merchant_record.contact_person = new_merchant_details.contact_person
        if new_merchant_details.contact_number:
            merchant_record.contact_number = new_merchant_details.contact_number
        if new_merchant_details.contact_email:
            merchant_record.contact_email = new_merchant_details.contact_email
        if new_merchant_details.address:
            merchant_record.address = new_merchant_details.address
        merchant_record.updated_at = time.time()
    db.session.add(merchant_record)
    db.session.commit()
    return merchant_record


def delete_merchant(merchant_id: str):
    merchant = db.session.query(Merchant).get(merchant_id)
    db.session.delete(merchant)
    db.session.commit()


def get_merchants(limit: int, offset: int):
    query = db.session.query(Merchant).order_by(Merchant.created_at.desc())
    merchant_list = _paginate(query, limit, offset)
    return merchant_list.all()


def _paginate(query, limit=None, offset=0):
    query = query.offset(offset)
    if limit:
        query = query.limit(limit)
    return query