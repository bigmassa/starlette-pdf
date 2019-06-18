from starlette.config import Config
from starlette.datastructures import URL, Secret

config = Config()


DEBUG = config("DEBUG", cast=bool, default=False)
SENTRY_DSN = config("SENTRY_DSN", cast=URL, default=None)

