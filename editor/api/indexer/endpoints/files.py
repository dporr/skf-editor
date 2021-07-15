from flask import request
from flask_restplus import Resource
from editor.api.indexer.business import get_files_output
from editor.api.indexer.serializers import files_response
from editor.api.restplus import api

ns = api.namespace('indexer', description='Operations related to terminal')

@ns.route('/files')
@api.response(404, 'Validation error', files_response)
class IndexerFiles(Resource):
    @api.marshal_with(files_response)
    @api.response(400, 'No results found', files_response)
    def get(self):
        """
        Returns a index of files of lab output.
        * Privileges required: **none**
        """
        result = get_files_output()
        return result, 200