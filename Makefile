.PHONY: install run clean create-env setup launch

install:
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

run:
	./venv/bin/python app.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

create-env:
	./venv/bin/python create_env.py

setup: clean install create-env

launch: setup run
