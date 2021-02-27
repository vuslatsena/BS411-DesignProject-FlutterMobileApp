from flask import Blueprint
from flask_restful import Api
from resources.register import register
from resources.signing import Signin
from resources.task import task
from resources.user import user
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(register, '/register')

api.add_resource(Signin, '/signin')

api.add_resource(task, '/tasks')

#from flask import Blueprint
#from flask import Api
#from resources.user import user

#api_bp = Blueprint('api', __name__)
#api = Api(api_bp)

# Routepyth
#api.add_resource(user, '/user')
# end point


##  Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#   Restarting with stat
#   Debugger is active!
#   Debugger PIN: xxx-xxx-xxx