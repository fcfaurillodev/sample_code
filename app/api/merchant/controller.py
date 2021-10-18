from flask import request
from app.api.merchant.json_format import __create_merchant, __update_merchant
from app.api import errors
from app.store.merchant import store
from app.store.merchant.model.merchant import Merchant
from app.utils.logging import logger
from app.config import Config
from typing import Optional


def get_merchant(merchant_id) -> dict:
    # get merchant details from db
    merchant = store.get_merchant(merchant_id=merchant_id)
    if merchant is None:
        raise errors.MerchantNotFound(f'Merchant with id {merchant_id} not found')
    return merchant.to_dict()


def get_merchants():
    limit = request.args.get('limit', Config.DEFAULT_PAGINATION_LIMIT)
    page = request.args.get('page', '1')

    # validate page and limit value
    if not _is_valid_request_args(limit=limit, page=page):
        raise errors.InvalidParameters(f'Page or Limit request param is invalid')

    offset = _get_offset(page=int(page), limit=int(limit))
    merchant_list = store.get_merchants(limit=int(limit), offset=offset)
    return merchant_list, page, limit


def create_merchant(body) -> dict:
    request_payload = __create_merchant.validate(body)
    logger.debug(f"[create_merchant] request body: {request_payload}")

    # check if merchant identity_id already exists
    if store.get_merchant_by_identity(identity_id=request_payload['identity_id']) is not None:
        raise errors.DuplicateMerchant(f'Merchant with identity_id {request_payload["identity_id"]} already exists')

    result = store.create_merchant(merchant=Merchant.from_dict(request_payload))
    return result.to_dict()


def update_merchant(merchant_id, body) -> dict:
    request_payload = __update_merchant.validate(body)
    logger.debug(f"[update_merchant] request body: {request_payload}")

    # check if merchant id exists
    merchant = store.get_merchant(merchant_id=merchant_id)
    if merchant is None:
        raise errors.MerchantNotFound(f'Merchant with id {merchant_id} not found')

    new_merchant_details = Merchant.from_dict(request_payload)
    result = store.update_merchant(merchant_id=merchant_id, new_merchant_details=new_merchant_details)
    return result.to_dict()


def delete_merchant(merchant_id):
    logger.debug(f"[delete_merchant] request to delete merchant with id: {merchant_id}")

    # check if merchant id exists
    merchant = store.get_merchant(merchant_id=merchant_id)
    if merchant is None:
        raise errors.MerchantNotFound(f'Merchant with id {merchant_id} not found')
    store.delete_merchant(merchant=merchant)


def _get_offset(page: int, limit: int):
    return (page - 1) * limit


def _is_valid_request_args(page, limit):
    if not limit.isnumeric() or int(limit) < 10:
        return False
    elif not page.isnumeric() or int(page) <= 0:
        return False
    else:
        return True
