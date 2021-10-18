import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    BASE_URL = os.environ.get('BASE_URL')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

    MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME')
    MYSQL_DB_HOST = os.environ.get('MYSQL_DB_HOST')
    MYSQL_DB_PORT = os.environ.get('MYSQL_DB_PORT')
    MYSQL_DB_USERNAME = os.environ.get('MYSQL_DB_USERNAME')
    MYSQL_DB_PASSWORD = os.environ.get('MYSQL_DB_PASSWORD')
    MYSQL_DB_CHARSET = os.environ.get('MYSQL_DB_CHARSET')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_DB_USERNAME}:{MYSQL_DB_PASSWORD}@{MYSQL_DB_HOST}/{MYSQL_DB_NAME}' \
                              f'?charset={MYSQL_DB_CHARSET}&binary_prefix=true'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = os.environ.get('REDIS_PORT')
    REDIS_DB = os.environ.get('REDIS_CACHE_DB')
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    REDIS_DECODE_RESPONSE = os.environ.get('REDIS_DECODE_RESPONSE')
    REDIS_SESSION_DB = os.environ.get('REDIS_SESSION_DB')
    REDIS_SESSION_TTL = os.environ.get('REDIS_SESSION_TTL')

    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
    LOG_FORMAT = os.environ.get('LOG_FORMAT', '%(asctime)s - %(levelname)s :: %(message)s')

    DEFAULT_PAGINATION_LIMIT = os.environ.get('DEFAULT_PAGINATION_LIMIT', '10')
    CACHE_TTL = int(os.environ.get('CACHE_TTL', 300))
    CACHE_LONG_TTL = int(os.environ.get('CACHE_LONG_TTL', 3600))


