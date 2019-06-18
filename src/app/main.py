from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles

from app import endpoints, handlers, settings

# base app
app = Starlette(debug=settings.DEBUG)

# routes
app.add_route("/", endpoints.Home, methods=["GET"], name="home")
app.add_route("/pdf/from-string", endpoints.FromString, methods=["GET", "POST"], name="from-string")
app.add_route("/pdf/from-url", endpoints.FromURL, methods=["GET", "POST"], name="from-url")

# exception handlers
app.add_exception_handler(404, handlers.not_found)
app.add_exception_handler(500, handlers.server_error)

# sentry
if settings.SENTRY_DSN:
    try:
        from sentry_asgi import SentryMiddleware
        import sentry_sdk

        sentry_sdk.init(str(settings.SENTRY_DSN))
        app = SentryMiddleware(app)
    except ImportError:
        pass