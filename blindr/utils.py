from datetime import datetime

def timestamp(dt):
    return (dt - datetime(1970,1,1)).total_seconds()
