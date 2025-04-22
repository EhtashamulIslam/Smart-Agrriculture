# Makefile for setting up and running the project

.PHONY: help venv activate install migrate run clean

help:
	@echo "Available targets:"
	@echo "  venv      - Create a virtual environment"
	@echo "  activate  - Activate the virtual environment"
	@echo "  install   - Install dependencies from requirements.txt"
	@echo "  migrate   - Apply database migrations"
	@echo "  run       - Start the development server"
	@echo "  clean     - Remove the virtual environment"

venv:
	python -m venv .venv

activate:
	@echo "Run the following command to activate the virtual environment:"
	@echo "On Windows: .\\.venv\\Scripts\\Activate"
	@echo "On macOS/Linux: source .venv/bin/activate"

install: venv
	.venv/bin/pip install -r requirements.txt

migrate:
	.venv/bin/python manage.py makemigrations
	.venv/bin/python manage.py migrate

run:
	.venv/bin/python manage.py runserver

clean:
	rm -rf .venv