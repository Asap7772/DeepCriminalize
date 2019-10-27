from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

todos = {}
class HelloWorld(Resource):
    def get(self, uid):
        return {'hello': str(uid)}

    def post(self, uid):
        json_data = request.get_json(force=True)
        return str(json_data)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
