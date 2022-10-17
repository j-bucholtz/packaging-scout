
create-venv:
	# Create a new python virtual environment
	python3 -m venv .venv;

update-deps:
	# Lock the app and dev dependencies
	python -m pip install --upgrade pip-tools pip wheel
	python -m piptools compile --upgrade -o requirements.txt pyproject.toml
	python -m piptools compile --extra dev --upgrade -o requirements-dev.txt pyproject.toml

prereqs:
	# Install the locked app and dev dependencies
	python -m pip install --upgrade pip wheel
	pip-sync requirements.txt  requirements-dev.txt

editable:
	python -m pip install --upgrade pip wheel
	python -m pip install requirements.txt requirements-dev.txt --editable .

update: update-deps prereqs

set-hooks:
	pre-commit install

run-hooks:
	pre-commit run --all-files

lint:
	black src/packaging_scout
	pylint src/packaging_scout
	mypy src/packaging_scout

.PHONY: create-venv update-deps prereqs update set-hooks run-hooks lint
