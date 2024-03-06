from flask import Flask,jsonify
from flask_restx import Resource,Api

# instantiate the app 

app = Flask(__name__) #

# The flask object implements a WSGI application and acts as the central object. 
# It is passed the name of the module or package of the application. 
# Once it is created it will act as a central registry for the view functions, 
# the URL rules, template configuration and much more.

api=Api(app)

# set config 
app.config.from_object('src.config.DevelopmentConfig')

class Ping(Resource):
    def get(self):
        return{
            "status":"sucess",
            "message":"pong"
        }
    
api.add_resource(Ping,'/ping')