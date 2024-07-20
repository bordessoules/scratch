from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import create_access_token

class RootResource(Resource):
    def get(self):
        return {"message": "Welcome to the API"}, 200

class LoginResource(Resource):
    def post(self):
        # This is a dummy login. In a real app, you'd verify credentials here.
        access_token = create_access_token(identity='user')
        return {"access_token": access_token}, 200

def initialize_routes(api):
    api.add_resource(RootResource, '/')
    api.add_resource(LoginResource, '/login')