FROM python:3.11-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install poetry

RUN poetry config installer.max-workers 10

COPY . .

RUN poetry install --no-interaction --no-ansi

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate --no-input && gunicorn project.wsgi:application --bind 0.0.0.0:8000"]

EXPOSE 8000