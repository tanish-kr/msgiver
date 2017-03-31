# Makefile for msgiver
#
# useful targets:
#		make test
#		make install
#		make clean
#		make build
#		make pep8

PWD = $(shell pwd)
OS = $(shell uname -s)
NAME = msgiver
PYTHON_VERSION = $(python --version)

test:
	python -m unittest tests

clean:
	@echo "Clean this project"
	rm -rf msgiver/msgiver.egg-info/
	find . -type f -regex ".*\.py[co]$$" -delete
	find . -type d -name "__pycache__"  -delete
	find . -type f \( -name "*.swp" \) -delete

watch:
	python bin/watcher.py
