from blindr import create_app
import config

app = create_app(config)
app.run()
