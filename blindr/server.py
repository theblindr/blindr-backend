from blindr import create_app
app = create_app('config.heroku')
app.logger.info('[server] init done')
