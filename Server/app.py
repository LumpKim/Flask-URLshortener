from flask import Flask, current_app
from flask_restful import Api
from mongoengine import connect

from Server.config import Config


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(Config)
    connect(current_app.config['MONGODB_URI'])

    from Server.view import URLHandling
    api.add_resource(URLHandling, '/<input_url>')

    return app
