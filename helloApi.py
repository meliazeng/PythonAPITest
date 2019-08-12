from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pymongo import Connection
from json import dumps
#from flask.ext.jsonpify import jsonify

connection = Connection('192.168.9.80', 31581)
db = connection.hellodb
app = Flask(__name__)
api = Api(app)

class Visit(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        
        if (args['name']):
            db.Visitors.insert({'Visit_name': args['name']})
            for visitor in db.Visitors.find():
                print visitor
            return 'hello ' + args['name']
        else:
            return 'hello stranger!'


api.add_resource(Visit, '/hello')

if __name__ == '__main__':
    app.run(debug=True, port='5002',host='192.168.9.60')
        

