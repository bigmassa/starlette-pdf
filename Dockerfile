ARG         EXTRA_DEPS="cairo-dev gdk-pixbuf-dev libffi-dev make pango-dev ttf-freefont"
ARG         REQUIREMENTS_FILE=/requirements/base.txt

FROM        accent/starlette-docker:3.8-alpine

ENV         APP_MODULE=app.main:app \
            ALLOWED_HOSTS="*" \
            SECRET_KEY="***** change me *****"

ENTRYPOINT  []

CMD         ["/start.sh"]
