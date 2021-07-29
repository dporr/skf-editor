from flask_restplus import fields
from editor.api.restplus import api


files_response = api.model('Files response message', {
    'lab_root_path': fields.String(required=True, description='Response message of terminal output'),
    'path': fields.String(required=True, description='The current pwd in termnial'),
    'size': fields.String(required=True, description='The current user in termnial'),
    'permissions': fields.String(required=True, description='The current user in termnial'),
})


files = api.inherit('List of files', {
    'files': fields.List(fields.Nested(files_response))
})