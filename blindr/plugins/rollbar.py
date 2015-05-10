from flask import Request, got_request_exception
import logging
import rollbar.contrib.flask
import rollbar

def init_rollbar(app):
    if 'ROLLBAR_TOKEN' in app.config:
        rollbar.init(
            app.config['ROLLBAR_ACCESS_TOKEN'],
            app.config['ENV'],
            root=os.path.dirname(os.path.realpath(__file__)),
            allow_logging_basic_config=False
        )

        got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

        logging.info('Initialized rollbar...')
