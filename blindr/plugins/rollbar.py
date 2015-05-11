from flask import Request, got_request_exception
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

        app.logger.info('[rollbar.init_rollbar] Rollbar enabled')
    else:
        app.logger.info('[rollbar.init_rollbar] Rollbar disabled')
