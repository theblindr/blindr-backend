import itsdangerous
from flask import request, abort
from functools import wraps

import config
from models import User

def token_authentication(token):
    if not token:
        return False

    s = itsdangerous.Signer(config.secret)
    user_id = False
    try:
        user_id = s.unsign(token)
    except itsdangerous.BadSignature:
        pass

    return config.session.query(User).filter_by(id=user_id).first()

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = token_authentication(request.headers.get('X-User-Token'))
        if user:
            func.im_self.user = user
            return func(*args, **kwargs)
        abort(401)
    return wrapper

