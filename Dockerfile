FROM python:3.12

# Definir variáveis de build (essas variáveis podem ser passadas durante o build)
ARG DB_HOST
ARG SECRET_KEY
ARG DEBUG

# Defina variáveis de ambiente
ENV DB_HOST=${DB_HOST}
ENV SECRET_KEY=${SECRET_KEY}
ENV DEBUG=${DEBUG}

# Set the poetry cache directory to /tmp
ENV POETRY_CACHE_DIR=/tmp/.cache/pypoetry

# Set the virtualenv location to /tmp/.cache
ENV VIRTUALENV_PATH=/tmp/.cache/pypoetry/virtualenvs

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

COPY ./backend /app/

RUN pip install poetry

RUN poetry config cache-dir /tmp/.cache/pypoetry

RUN poetry install --no-root

RUN ls /app/

CMD poetry run python /app/manage.py migrate && poetry run gunicorn --bind 0.0.0.0:8000 core.wsgi:application