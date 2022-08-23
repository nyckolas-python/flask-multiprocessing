# Makefile
#!/bin/bash

start:
	export SECRET_KEY="SECRET_KEY" && \
	poetry run python wsgi.py

update:
	sudo apt update && poetry update

install:
	poetry install

build:
	poetry build

package-install:
	pip install --user dist/*.whl


# Makefile last line
# ignores existing files
.PHONY: install build