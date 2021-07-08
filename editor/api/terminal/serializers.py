from flask_restplus import fields
from editor.api.restplus import api


terminal_cmd = api.model('terminal', {
    'command': fields.String(required=True, description='The command to be excecuted in termnial'),
})


terminal_response = api.model('Terminal response message', {
    'output': fields.String(required=True, description='Response message of terminal output'),
    'cwd': fields.String(required=True, description='The current pwd in termnial'),
    'user': fields.String(required=True, description='The current user in termnial'),
})