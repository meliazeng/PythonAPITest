from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pymongo import Connection
from json import dumps

# connection string for mongo db
connection = Connection('localhost', 27017)
db = connection.hellodb
app = Flask(__name__)
api = Api(app)

class Visit(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        # get post body
        parser.add_argument('name')
        args = parser.parse_args()
        
        if (args['name']):
            # save the recode to mongo if the post contain valid name
            db.Visitors.insert({'Visit_name': args['name']})
            for visitor in db.Visitors.find():
                print visitor
            return 'hello ' + args['name']
        else:
            # skip the save and return message. 
            return 'hello stranger!'


api.add_resource(Visit, '/hello')

if __name__ == '__main__':
    # run the api on localhost and open port 5002
    app.run(debug=True, port='5002',host='localhost')
        

