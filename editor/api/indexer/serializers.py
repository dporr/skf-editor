from flask_restplus import fields
from editor.api.restplus import api


files_response = api.model('Files response message', {
    'files': fields.Raw(required=True, description='Response message of terminal output'),
})

filecontent_response = api.model('Files response message', {
    'hash': fields.String(required=True, description='Response message of terminal output'),
})


files = api.inherit('List of files', {
    'files': fields.List(fields.Nested(files_response))
})