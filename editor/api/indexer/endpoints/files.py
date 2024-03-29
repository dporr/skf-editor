from flask import request
from flask_restplus import Resource
from editor.api.indexer.business import get_files_output, open_file, save_file
from editor.api.indexer.serializers import files_response,filecontent_response,filecontent
from editor.api.restplus import api

ns = api.namespace('indexer', description='Operations related to files')

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

@ns.route('/files/<id>')
@api.response(404, 'Validation error')
class IndexerFiles(Resource):
    @api.marshal_with(filecontent_response)
    @api.response(400, 'No results found')
    def get(self,id):
        """
        Returns the file contents based on the file hash id
        * Privileges required: **none**
        """
        result = open_file(id)
        return result, 200

@ns.route('/files')
@api.doc(filecontent)
@api.response(404, 'Validation error', filecontent_response)
class IndexerFiles(Resource):
    @api.expect(filecontent)
    @api.marshal_with(filecontent_response)
    @api.response(400, 'No results found', filecontent_response)
    def put(self):
        """
        Saves the file based on the hash id received in the json payload
        * Privileges required: **none**
        """
        data = request.json
        print(request.json)
        id = data.get('hash', "")
        content = data.get('content', "")
        result = save_file(id, content)
        return result, 200