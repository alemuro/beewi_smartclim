SHELL := /bin/bash

build: dist

.ONESHELL:
dist: virtualenv
	source virtualenv/bin/activate
	python setup.py sdist bdist_wheel

.ONESHELL:
publish: dist
	source virtualenv/bin/activate
	pip install twine
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.ONESHELL:
publish-live: dist
	source virtualenv/bin/activate
	pip install twine
	twine upload dist/*

clean:
	rm -rf virtualenv dist build beewi_smartclim.egg-info beewi_smartclim/*.pyc **/__pycache__

virtualenv: 
	virtualenv virtualenv --python=python3

.ONESHELL:
test: virtualenv dist
	source virtualenv/bin/activate
	python --version
	pip install -r requirements.txt
	python test.py