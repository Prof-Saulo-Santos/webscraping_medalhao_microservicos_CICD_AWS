.PHONY: test coverage lint run

test:
	poetry run pytest tests/ -v

coverage:
	poetry run pytest --cov=app tests/

lint:
	poetry run ruff check .
	poetry run black --check .

run:
	poetry run uvicorn app.api:app --reload --host 0.0.0.0 --port 8000

bump-patch:
	poetry run bump2version patch

bump-minor:
	poetry run bump2version minor

bump-major:
	poetry run bump2version major