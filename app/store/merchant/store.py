from app.store.merchant import service, cache
from app.store.merchant.model.merchant import Merchant
from typing import Optional
import time


def get_merchant(merchant_id: str) -> Optional[Merchant]:
    """ Returns Merchant object with merchant_id """
    # check cache
    cache_result= cache.get_merchant(merchant_id=merchant_id)
    if cache_result:
        return Merchant.from_str(cache_result)
    else:
        # query from db
        db_result = service.get_merchant(merchant_id=merchant_id)
        if db_result:
            # save result to cache
            cache.set_merchant(merchant_id=merchant_id, merchant_details=db_result.to_str())
        return db_result


def create_merchant(merchant: Merchant) -> Merchant:
    """ Insert new merchant record into db """
    # insert into db
    res = service.create_merchant(merchant=merchant)
    # delete existing cache
    cache.delete_merchants()
    return res


def get_merchant_by_identity(identity_id) -> Optional[Merchant]:
    """ Returns Merchant object with identity_id """
    # check cache
    cache_result= cache.get_merchant_by_identity(identity_id=identity_id)
    if cache_result:
        return Merchant.from_str(cache_result)
    else:
        # query from db
        db_result = service.get_merchant_by_identity(identity_id=identity_id)
        if db_result:
            # save result to cache
            cache.set_merchant_by_identity(identity_id=identity_id, merchant_details=db_result.to_str())
        return db_result


def update_merchant(merchant_id: str, new_merchant_details: Merchant) -> Merchant:
    """ Update merchant record in db """
    # update db record
    res = service.update_merchant(merchant_id=merchant_id, new_merchant_details=new_merchant_details)
    if res:
        # delete existing cache
        cache.delete_merchant(merchant_id=merchant_id)
        cache.delete_merchants()
    return res


def delete_merchant(merchant: Merchant):
    """ Delete merchant in db """
    # delete db record
    service.delete_merchant(merchant_id=merchant.id)
    # delete existing cache
    cache.delete_merchants()
    cache.delete_merchant(merchant_id=merchant.id)
    cache.delete_merchant_by_identity(identity_id=merchant.identity_id)


def get_merchants(limit: int, offset: int) -> [Merchant]:
    """ Returns Merchant list within the limit set """
    # check cache with filter
    filter = f'{limit}:{offset}'
    cache_result= cache.get_merchants(field=filter)
    if cache_result:
        return Merchant.from_str(cache_result)
    else:
        # query from db
        db_result = service.get_merchants(limit=limit, offset=offset)
        if len(db_result) > 0:
            formatted_merchant_list = Merchant.from_list(db_result)
            merchant_list_details = Merchant.to_str_list(formatted_merchant_list)
            # save result to cache
            cache.set_merchants(field=filter, merchant_details=merchant_list_details)
            return formatted_merchant_list
        else:
            return []
