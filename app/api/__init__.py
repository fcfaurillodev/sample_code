from app.api.healthcheck.routes import healthcheck
from app.api.merchant.routes import merchant
from app.utils.logging import logger


def init_app(app):
    app.register_blueprint(healthcheck)
    app.register_blueprint(merchant)

    @app.errorhandler(Exception)
    def publish_error(error):
        logger.exception(error)
        return {'message': 'unknown error occurred'}, 500

    @app.errorhandler(404)
    def page_not_found(e):
        return {'message': 'page not found'}, 404
