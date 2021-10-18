from flask import Blueprint, jsonify

healthcheck = Blueprint('healthcheck', __name__, url_prefix='/api')

@healthcheck.route('/healthcheck', methods=['GET'])
def healthcheck_endpoint():
    return jsonify({'message': 'ok'}), 200