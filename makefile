PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python

# Test if python is installed
ifeq (,$(shell $(PYTHON_INTERPRETER) --version))
$(error "Python is not installed!")
endif


.PHONY: clean_migrations
clean_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "./venv/*" -delete
	find . -path "*/migrations/*.pyc" -not -path "./venv/*" -delete


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
	sass core/static/scss/volt.scss core/static/css/volt.css

black:
	black . --line-length 79 --exclude venv