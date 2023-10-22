PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python

# Test if python is installed
ifeq (,$(shell $(PYTHON_INTERPRETER) --version))
$(error "Python is not installed!")
endif


.PHONY: clean_migrations
clean_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "./.venv/*" -not -path "./venv/*" -not -path "*/home/migrations/0001_create_database_views.py" -delete
	find . -path "*/migrations/*.pyc" -not -path "./.venv/*" -not -path "./venv/*" -not -path "*/home/migrations/0001_create_database_views.pyc" -delete
	rm db.sqlite3

install-pip-tools:
	$(PYTHON_INTERPRETER) -m pip install pip-tools


pip-compile: install-pip-tools
	pip-compile --no-emit-index-url requirements.in
	pip-compile --no-emit-index-url requirements-dev.in


requirements: pip-compile
	$(PYTHON_INTERPRETER) -m pip install -r requirements-dev.txt &&\
	pre-commit install
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Synchronize the Python Dependencies & Virtual Env
sync-env: pip-compile
	pip-sync requirements.txt requirements-dev.txt

scss:
	sass core/scss/volt.scss core/static/css/volt.css

black:
	black . --line-length 79 --exclude venv

# generate a new django secret key and copy it to .env file in the form SECRET_KEY=...
django-secret-key:
	$(PYTHON_INTERPRETER) -c 'from django.core.management.utils import get_random_secret_key; print("SECRET_KEY=" + get_random_secret_key())' >> .env
