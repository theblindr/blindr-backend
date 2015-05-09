import itsdangerous
from flask import request, abort, current_app
from functools import wraps
from blindr.models.user import User

def token_authentication(token):
    if not token:
        return False

    s = itsdangerous.Signer(current_app.config['AUTH_SECRET'])
    user_id = False
    try:
        user_id = s.unsign(token).decode('utf-8')
    except itsdangerous.BadSignature:
        pass

    return User.query.get(user_id)

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = token_authentication(request.headers.get('X-User-Token'))
        if user:
            func.__self__.user = user
            return func(*args, **kwargs)
        abort(401)
    return wrapper

