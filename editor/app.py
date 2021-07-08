#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
    Security Knowledge Framework Editor is part of SKF.
    Copyright (C) 2021 Glenn ten Cate, Riccardo ten Cate
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import logging.config
from flask import Flask, Blueprint
from flask_cors import CORS, cross_origin
from editor import settings

from editor.api.terminal.endpoints.terminal import ns as terminal_namespace
from editor.api.restplus import api

def create_app():
    flask_app = Flask(__name__)
    configure_app(flask_app)
    initialize_app(flask_app)
    return flask_app


def configure_app(flask_app):
    """Configure the SKF Editor app."""
    #cannot use SERVER_NAME because it will mess up the routing
    flask_app.config['TESTING'] = settings.TESTING
    flask_app.config['FLASK_DEBUG'] = settings.FLASK_DEBUG


def initialize_app(flask_app):
    """Initialize the SKF Editor app."""
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(terminal_namespace)
    flask_app.register_blueprint(blueprint)

app = create_app()
cors = CORS(app, resources={r"/api/*": {"origins": settings.ORIGINS}})
log = logging.getLogger(__name__)


def main():
    """Main SKF editor method"""
    if settings.FLASK_DEBUG == 'False':
        log.info('>>>>> Starting development server http://'+settings.FLASK_HOST+":"+str(settings.FLASK_PORT)+' <<<<<')
        app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=False)    
    else:
        log.info('>>>>> Starting development server http://'+settings.FLASK_HOST+":"+str(settings.FLASK_PORT)+' <<<<<')
        app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=True)


if __name__ == "__main__":
    main()