import logging
from app.config import Config
from datetime import datetime

# Create a custom logger
logger = logging.getLogger(__name__)


def init_log():
    """ Initialize logger config (log level, handler) """
    logger.setLevel(Config.LOG_LEVEL)
    # Create handler
    stream_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    formatter = logging.Formatter(Config.LOG_FORMAT)
    stream_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(stream_handler)