from flask import g
from functools import wraps
from app.config import Config
from app.api.errors import InvalidToken, InvalidRequestHeaders
from app.utils.jwt_authentication import JWTAuthentication
from app.utils.logging import logger
from app.store.client import store


def validate_request_headers(request):
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            # check request header format
            client_id, token = _check_request_headers(request)

            # check if client id is active
            client = store.get_client(client_id=client_id)
            if client is None or (client and not client.active):
                raise InvalidRequestHeaders('Client ID not found in client list')

            # validate jwt token
            decoded_payload = _validate_token(token, client)
            return function(*args, **kwargs)
        return decorated
    return decorator


def _check_request_headers(request):
    auth_header = request.headers.get('Authorization')
    client_id = request.headers.get('client-id')

    if client_id is None or auth_header is None:
        raise InvalidRequestHeaders('client-id or Authorization header is missing')

    auth_parts = auth_header.split(' ')
    if len(auth_parts) != 2:
        raise InvalidRequestHeaders('Malformed authorization header')

    return client_id, auth_parts[1]


def _validate_token(token, client):
    try:
        logger.debug(f'[validate_request_headers][_validate_token] Validating request token {token} for Client {client.client_id}')
        return JWTAuthentication(audience=client.audience, pub_key=client.pub_key).decode(token)
    except Exception as e:
        raise InvalidToken(e)
