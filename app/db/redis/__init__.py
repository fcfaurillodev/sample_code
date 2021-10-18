from app.config import Config
import redis

redis_client = redis.StrictRedis(host=Config.REDIS_HOST,
                                 port=Config.REDIS_PORT,
                                 db=Config.REDIS_DB,
                                 password=Config.REDIS_PASSWORD,
                                 decode_responses=Config.REDIS_DECODE_RESPONSE)