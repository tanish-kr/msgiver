# Makefile for msgiver
#
# useful targets:
#		make test
#		make install
#		make update
#		make clean
#		make develop
#		make watch

PWD = $(shell pwd)
OS = $(shell uname -s)
NAME = msgiver
PYTHON_VERSION = $(python --version)

test:
	python -m unittest tests

build-pkg: clean
	@echo "Build to setup.py"
	python setup.py sdist
	twine register dist/*

upload-pkg:
	@echo "Upload package to PyPI"
	twine upload dist/*

install: clean
	@echo "Install msgiver"
	python setup.py install
	@echo "Complete installed msgiver"

update:
	@echo "Update msgiver"
	python setup.py install
	unlink /usr/local/bin/msgiver
	ln -svf ./bin/msgiver /usr/local/bin
	/usr/local/bin/msgiver setting
	@echo "Complete updated msgiver"

clean:
	@echo "Clean this project"
	rm -rf msgiver.egg-info/
	rm -rf dist/*
	rm -rf build/*
	find . -type f -regex ".*\.py[co]$$" -delete
	find . -type d -name "__pycache__"  -delete
	find . -type f \( -name "*.swp" \) -delete

develop:
	@echo "Development msgiver project"
	pip install -r requirements/dev.txt
	@echo "This project document is <https://github.com/kitaro-tn/msgiver/blob/master/README.md>"

watch:
	python bin/watcher.py
