# checkout-service

A tiny example service used to demonstrate Operate integrations.

## Stack

- Python 3.11
- FastAPI
- PostgreSQL

## Local setup

    pipenv install
    pipenv run uvicorn app.main:app --reload

## Running tests

    pipenv run pytest

## Environment

Copy `.env.example` to `.env` and fill in the required values.

Connected to operate

## API

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Returns service health status. Responds with `{"status": "ok"}` when the service is running. |
| `POST` | `/checkout` | Creates a new order and returns the generated order ID. |

Licensed under MIT.
