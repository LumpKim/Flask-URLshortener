from flask import request, redirect, Response, current_app
from flask_restful import Resource
from Server.model import URLModel
from base62 import encode, decode


class URLHandling(Resource):

    def get(self, input_url):

        data = URLModel.objects(link=encode(input_url)).first()
        destination = 'http://' + current_app.config['SERVER_NAME'] + '/' + data.link

        redirect(destination)

    def post(self):

        # json 으로 줄이려는 원본 url 받아오기
        input_url = request.json['input_url']

        # DB 에 input_url 저장
        URLModel(link=input_url)

        # url 생성 과정
        if current_app.config['SERVER_NAME']:
            host = current_app.config['SERVER_NAME']

        else:
            host = 'localhost'

        return {'output_url': 'http://{}/{}'.format(host, decode(input_url))}
