from app.db.redis import redis_client
from app.config import Config

"""
Redis operations for caching merchant data
"""

_merchant_key = 'merchant'
_merchant_identity_key = 'merchant:identity'
_merchant_hash_key = 'merchants'
_ttl = Config.CACHE_TTL
_long_ttl = Config.CACHE_LONG_TTL


def get_merchant(merchant_id: str):
    return redis_client.get(f'{_merchant_key}:{merchant_id}')

def set_merchant(merchant_id: str, merchant_details: str):
    return redis_client.setex(f'{_merchant_key}:{merchant_id}', _ttl, merchant_details)

def delete_merchant(merchant_id):
    return redis_client.delete(f'{_merchant_key}:{merchant_id}')

def get_merchant_by_identity(identity_id: str):
    return redis_client.get(f'{_merchant_identity_key}:{identity_id}')

def set_merchant_by_identity(identity_id: str, merchant_details: str):
    return redis_client.setex(f'{_merchant_identity_key}:{identity_id}', _ttl, merchant_details)

def delete_merchant_by_identity(identity_id):
    return redis_client.delete(f'{_merchant_identity_key}:{identity_id}')

def expire_merchants():
    return redis_client.expire(_merchant_hash_key, _ttl)

def get_merchants(field: str):
    return redis_client.hget(_merchant_hash_key, field)

def set_merchants(field: str, merchant_details: str):
    return redis_client.hset(_merchant_hash_key, field, merchant_details)

def delete_merchants():
    return redis_client.delete(_merchant_hash_key)