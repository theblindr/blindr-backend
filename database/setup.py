from models import Match, User
import config

Base.metadata.create_all(config.engine)
