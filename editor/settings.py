import os

# Flask settings
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 1337

# Do not use debug mode in production
FLASK_DEBUG = (os.environ.get("SKF_EDITOR_DEBUG") == 'True') or False
ORIGINS = '*'

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# TESTING settings
TESTING = (os.environ.get("SKF_EDITOR_TESTING") == 'True') or False
