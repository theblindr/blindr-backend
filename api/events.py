from flask.ext import restful
from authenticate import authenticate

class Events(restful.Resource):
    method_decorators=[authenticate]
    def get():
        # Get events since last poll
        pass

    def post():
        event_type = request.form.get('type')
        pass


