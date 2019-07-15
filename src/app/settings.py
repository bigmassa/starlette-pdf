from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, URL, Secret

config = Config()


ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=CommaSeparatedStrings)
DEBUG = config("DEBUG", cast=bool, default=False)
SENTRY_DSN = config("SENTRY_DSN", cast=URL, default=None)

