import logging

from flask_restplus import Api
from editor import settings

log = logging.getLogger(__name__)


api = Api(version='1.0', title='OWASP-SKF Editor API',
          description='OWASP-SKF Flask Editor RestPlus powered API')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    if not settings.FLASK_DEBUG:
        return {'message': message}, 500

