FROM python:3.12-slim

WORKDIR /service

COPY pyproject.toml poetry.lock* Makefile ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY app ./app

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]