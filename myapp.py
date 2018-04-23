from flask import Flask
from flask_restful import Resource, Api, reqparse
import os

parser = reqparse.RequestParser()
parser.add_argument('key')

app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def get(self):
        args = parser.parse_args()
        return {'key': args['key']}

api.add_resource(MyResource, '/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
