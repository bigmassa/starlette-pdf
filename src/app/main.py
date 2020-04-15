from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from app import endpoints, globals, handlers, settings

routes = [
    Route("/", endpoints.Home, methods=["GET"], name="home"),
    Route(
        "/from-string",
        endpoints.FromString,
        methods=["GET", "POST"],
        name="from-string",
    ),
    Route("/from-url", endpoints.FromURL, methods=["GET", "POST"], name="from-url"),
]

middleware = [
    Middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS),
]

exception_handlers = {
    404: handlers.not_found,
    500: handlers.server_error,
}

app = Starlette(
    debug=settings.DEBUG,
    routes=routes,
    middleware=middleware,
    exception_handlers=exception_handlers,  # type: ignore
)

if settings.SENTRY_DSN:
    try:
        from sentry_asgi import SentryMiddleware
        import sentry_sdk

        sentry_sdk.init(str(settings.SENTRY_DSN))
        app = SentryMiddleware(app)
    except ImportError:
        pass
