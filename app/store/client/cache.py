from app.db.redis import redis_client
from app.config import Config

"""
Redis operations for caching client data
"""

_client_key = 'clients'
_ttl = Config.CACHE_TTL


def get_client(client_id: str):
    return redis_client.get(f'{_client_key}:{client_id}')


def set_client(client_id: str, client_details: str):
    return redis_client.setex(f'{_client_key}:{client_id}', _ttl, client_details)