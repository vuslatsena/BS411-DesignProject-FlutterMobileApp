from flask_restful import Resource
from flask import request
from Model import db, User
import random
import string

class signIn(Resource):
    def post(self):
        result = " "
        json_data = request.get_json(force=True)
        header = request.headers["Authorization"]

        if not header:
            result = self.username_and_password_signin(json_data)
        else:
            user = User.query.filter_by(api_key=header).first()
            if user:
                result = User.serialize(user)
            else:
                result = self.username_and_password_signin(json_data)

        return {"status": 'success', 'data': result}, 202

    def username_and_password_signin(self, json_data):
        if not json_data:
            return {'message': 'No input data provided'}, 400

        user = User.query.filter_by(username=json_data['username']).first()
#incorrect password
        if user.password != json_data['password']: 
            return {'message': 'Password incorrect'}, 400
#incorrect username
        if not user:
            return {'message': 'Username does not exist'}, 400
        return User.serialize(user)

    def generate_key(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(50))

#self represents the instance of the class. 
# By using the “self” keyword we can access the attributes and methods of the class in python. 
# It binds the attributes with the given arguments.