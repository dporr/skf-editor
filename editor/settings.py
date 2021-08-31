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

#SKF lab variables
SKF_LAB_DOMAIN = os.getenv("SKF_LAB_DOMAIN", "localhost")
SKF_LAB_PORT = os.getenv("SKF_LAB_PORT", 6667)
SKF_EDITOR_DOMAIN = os.getenv("SKF_EDITOR_DOMAIN", FLASK_HOST)
SKF_EDITOR_PORT = os.getenv("SKF_EDITOR_PORT", FLASK_PORT)