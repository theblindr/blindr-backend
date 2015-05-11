from logentries
import logging

def init_logging(app):
    app.logger.addHandler(logging.StreamHandler())
    app.logger.addHandler(logentries.LogentriesHandler('25ad6a50-0ab3-41d8-ab1c-416904d00992'))
    app.logger.setLevel(logging.INFO)
