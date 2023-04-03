.PHONY: clean_migrations
clean_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "./venv/*" -delete
	find . -path "*/migrations/*.pyc" -not -path "./venv/*" -delete