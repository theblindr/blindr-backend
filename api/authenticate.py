import itsdangerous
from flask import request, abort
from functools import wraps

import config

def token_authentication(token):
    if not token:
        return False

    s = itsdangerous.Signer(config.secret)
    user = False
    try:
        user = s.unsign(token)
    except itsdangerous.BadSignature:
        pass
    return user

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = token_authentication(request.headers.get('X-User-Token'))
        if user:
            func.im_self.user = user
            return func(*args, **kwargs)
        abort(401)
    return wrapper

