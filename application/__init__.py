from __future__ import absolute_import
from flask import Flask
from application import configuration as config
from application.routing import router as base_router
from application.routing.pages import router as pages_router
from application.routing.docker import router as docker_router

server = Flask(
    __name__,
    template_folder=config.template_folder
)

server.register_blueprint(base_router)
server.register_blueprint(pages_router, url_prefix='/pages')
server.register_blueprint(docker_router, url_prefix='/docker')
#app.register_blueprint()