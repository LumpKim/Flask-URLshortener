from functools import wraps
from unittest import TestCase

from Server.app import create_app
from mongoengine import connect
from mongoengine.connection import _get_db


class TestCaseBase(TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.mongodb = self.app.config['MONGODB_URI']
        connect(self.mongodb)

    def tearDown(self):
        db = _get_db
        db.connection.drop_database(self.mongodb)

    def save_url_request(self, url = 'http://blog.jaehoon.kim'):
        rv = self.client.post('/', json={'output_url': url})
        return rv

    def get_url_request(self, url):
        rv = self.client.get('/' + url)
        return rv


def check_status_code(status_code):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            rv = fn(self, *args, **kwargs)
            self.assertEqual(rv.status_code, status_code)
        return wrapper
    return decorator
