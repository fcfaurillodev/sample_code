from flask import Flask, g, request
from app.config import Config
from app.api import init_app as register_routes
from app.db.mysql import db
from app.utils.logging import init_log, logger
import datetime
import time


def create_app(test_config=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_object(Config)

    # initialize db config
    db.init_app(application)

    # initialize logging config
    init_log()

    # add routes
    register_routes(application)

    with application.app_context():
        db.create_all()

    @application.before_request
    def start_timer():
        g.start = time.time()


    @application.after_request
    def log_request(response):
        now = time.time()
        execution_time = round(now - g.start, 2)
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        host = request.host.split(':', 1)[0]
        args = dict(request.args)

        from app.utils.logging import logger
        logger.debug(f'Request Log: {request.method} {request.path} status: {response.status_code} '
                     f'response time: {execution_time}(s) ip: {ip} host: {host} params: {args}')
        return response

    @application.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()
        if exception and db.session.is_active:
            from app.utils.logging import logger
            logger.debug('teardown_appcontext :: shutdown_session :: Exception {}'.format(repr(exception)))
            db.session.rollback()

    @application.teardown_request
    def session_clear(exception=None):
        db.session.remove()
        if exception and db.session.is_active:
            from app.utils.logging import logger
            logger.debug('teardown_request :: session_clear :: Exception {}'.format(repr(exception)))
            db.session.rollback()


    return application