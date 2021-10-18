import jwt
from app.utils.logging import logger


class JWTAuthentication:
    """
    Python class thar represents jwt authentication
    """
    def __init__(self, audience: str ='', pub_key: str = '', private_key: str = ''):
        self._audience = audience
        self._pub_key = pub_key
        self._private_key = private_key

    def encode(self, payload):
        """
        Returns JWT encoded token
        """
        return jwt.encode(payload, self._private_key, algorithm='RS256')

    def decode(self, token):
        """
        Returns JWT decoded payload
        Parameters
        ----------
        token
            String token to decode
        Returns
        -------
        dict
            decoded payload
        """
        try:
            return jwt.decode(token, self._pub_key, audience=self._audience, algorithms='RS256')
        except Exception as exception:
            logger.error(f'[JWTAuthentication][decode] {exception}')
            raise InvalidAuthorizationToken('Failed to decode JWT token')