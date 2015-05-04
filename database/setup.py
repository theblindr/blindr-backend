from models import *
import config

Base.metadata.create_all(config.engine)
