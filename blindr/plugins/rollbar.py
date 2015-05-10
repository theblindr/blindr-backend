from flask import Request, got_request_exception
import rollbar.contrib.flask
import rollbar

def init_rollbar(app):
    if 'ROLLBAR_TOKEN' in app.config:
        @app.before_first_request
        def _init_rollbar():
            rollbar.init(
                app.config['ROLLBAR_TOKEN'],
                app.config['ENV'],
                root=os.path.dirname(os.path.realpath(__file__)),
                allow_logging_basic_config=False
            )

            got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
