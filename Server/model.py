from mongoengine import *
from datetime import datetime


class URLModel(Document):
    id = IntField(primary_key=True)
    link = StringField(required=True)
    generated_date = DateTimeField(default=datetime.utcnow)

