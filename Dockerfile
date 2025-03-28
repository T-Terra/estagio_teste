FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

COPY ./backend/ /app/

RUN pip install poetry

RUN poetry install --no-root --no-dev

RUN poetry run python manage.py migrate

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "backend.core.wsgi:application"]