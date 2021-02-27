#User:
#String userID;
#String apiKey;
#String firstName;
#String lastName;
#String email;
#String password;

#from flask_restful import resources
#from flasktest import api 
#class User(resources):
#def get(self) :
#        return {"message": "Hello, World!"}
        
#Expected indented blockPylance: This means that a function must have at least one line of code
#It also means that a conditional must have at least one line of code to run if the condition is true

from flask_restful import resources
class user(resources):
    def __init__(self,userID,api) -> None:
        super().__init__()

        