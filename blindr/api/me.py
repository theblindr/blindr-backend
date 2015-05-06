from flask.ext import restful
from .authenticate import authenticate

class Me(restful.Resource):
    method_decorators=[authenticate]
    def get(self):
        return {
            'id': self.user.id,
            'gender': self.user.gender
        }

