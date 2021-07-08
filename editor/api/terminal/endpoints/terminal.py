from flask import request
from flask_restplus import Resource
from editor.api.terminal.business import get_terminal_output
from editor.api.terminal.serializers import terminal_response, terminal_cmd
from editor.api.restplus import api

ns = api.namespace('terminal', description='Operations related to terminal')

@ns.route('/command')
@api.doc(terminal_cmd)
@api.response(404, 'Validation error', terminal_response)
class TerminalCMD(Resource):
    @api.expect(terminal_cmd)
    @api.marshal_with(terminal_response)
    @api.response(400, 'No results found', terminal_response)
    def post(self):
        """
        Returns a terminal command output.
        * Privileges required: **none**
        """
        data = request.json
        cmd = data.get('command')
        result = get_terminal_output(cmd)
        return result, 200