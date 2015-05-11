import logging

def init_logging(app):
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
