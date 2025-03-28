FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

COPY ./backend /app/

RUN pip install poetry

RUN poetry install --no-root

RUN ls /app/

CMD poetry run python /app/manage.py migrate && poetry run gunicorn --bind 0.0.0.0:8000 core.wsgi:application