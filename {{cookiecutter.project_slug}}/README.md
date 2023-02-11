
# Welcome to your Python API project!

This project is intended for use for builing REST API using the following libraries:
* [FastAPI](https://fastapi.tiangolo.com/) light weight API framework
* [SQLalchemy](https://www.sqlalchemy.org/) Sqlite and PostgreSQL async support are included
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) database migration

The following dev tooling are pre-configured:

* black
* flake8
* isort
* mypy
* VS Code support

## Setup

```shell

# install dependencies
poetry install
poetry export --without-hashes --format=requirements.txt > requirements.txt
poetry export --dev --without-hashes --format=requirements.txt > requirements-dev.txt
poetry run pre-commit install
poetry shell

# setup config and database
cp env.txt .env
alembic upgrade head
pytest -s -v

# linting, optional
black .
isort **/*.py
flake8
mypy .

```

## Get to work

```shell
# run unit tests
pytest -s -v

```
