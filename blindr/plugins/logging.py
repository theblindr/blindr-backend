import logging

def init_logging(app):
    if app.config['LOGGING_ENABLED']:
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(app.config['LOGGING_LEVEL'])
