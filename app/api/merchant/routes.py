from flask import Blueprint, request, jsonify
from app.api import errors
from app.api.merchant import controller
from app.utils.logging import logger
from app.decorators.authentication import validate_request_headers
import traceback

merchant = Blueprint('merchant', __name__,  url_prefix='/api')


@merchant.route('/merchant/<int:merchant_id>', methods=['GET'])
@validate_request_headers(request)
def get_merchant(merchant_id):
    merchant = controller.get_merchant(merchant_id)
    return jsonify(merchant), 200


@merchant.route('/merchants', methods=['GET'])
@validate_request_headers(request)
def get_merchants():
    merchants, page, limit = controller.get_merchants()
    return jsonify({
        'merchants': merchants,
        'page': page,
        'limit': limit
    }), 200


@merchant.route('/merchant', methods=['POST'])
@validate_request_headers(request)
def create_merchant():
    merchant = controller.create_merchant(request.json)
    return jsonify(merchant), 201


@merchant.route('/merchant/<int:merchant_id>', methods=['PATCH'])
@validate_request_headers(request)
def update_merchant(merchant_id):
    merchant = controller.update_merchant(merchant_id, request.json)
    return jsonify(merchant), 200


@merchant.route('/merchant/<int:merchant_id>', methods=['DELETE'])
@validate_request_headers(request)
def delete_merchant(merchant_id):
    controller.delete_merchant(merchant_id)
    return jsonify({"status": "Ok"}), 200


@merchant.errorhandler(errors.InvalidParameters)
def invalid_parameters(e):
    logger.error(f'[Merchant API] {e.message} :: {e.details}')
    return jsonify({
       'code': e.code,
       'message': e.message,
       'details': e.details
   }), 400


@merchant.errorhandler(errors.InvalidRequestHeaders)
def invalid_request_header(e):
    logger.error(f'[Merchant API] {e.message} :: {e.details}')
    return jsonify({
       'code': e.code,
       'message': e.message,
       'details': e.details
   }), 400


@merchant.errorhandler(errors.InvalidToken)
def invalid_token(e):
    logger.error(f'[Merchant API] {e.message} :: {e.details}')
    return jsonify({
       'code': e.code,
       'message': e.message,
       'details': e.details
   }), 401


@merchant.errorhandler(errors.MerchantNotFound)
def merchant_not_found(e):
    logger.error(f'[Merchant API] {e.message} :: {e.details}')
    return jsonify({
       'code': e.code,
       'message': e.message,
       'details': e.details
   }), 404


@merchant.errorhandler(errors.DuplicateMerchant)
def duplicate_merchant(e):
    logger.error(f'[Merchant API] {e.message} :: {e.details}')
    return jsonify({
       'code': e.code,
       'message': e.message,
       'details': e.details
   }), 409


@merchant.errorhandler(Exception)
def generic_error(e):
    logger.error(f'[Merchant API] Generic Error: {e}')
    logger.error(f'[Merchant  API] {traceback.format_exc()}')
    return jsonify({
       'code': '5001',
       'message': 'System Error'
   }), 500