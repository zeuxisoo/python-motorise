.PHONY: clean clean-pyc test test-env create-dist

all:
	@echo
	@echo "Command          : Description"
	@echo "---------------- : ------------"
	@echo "make env         : Create virtualenv"
	@echo "make test        : Run the test cases"
	@echo "make clean       : Clean the project generated files"
	@echo "make clean-build : Clean the generated build files only"
	@echo "make dist-tools  : Install the publish tools"
	@echo

env:
	@python3 -m venv venv3
	@venv3/bin/pip install --upgrade pip
	@venv3/bin/pip install -r requirements.txt

clean: clean-build clean-pyc

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

test:
	@venv3/bin/py.test tests

dist-tools:
	@venv3/bin/pip install wheel
	@venv3/bin/pip install twine

create-dist: clean
	@python setup.py sdist bdist_wheel

upload-dist:
	@python -m twine upload dist/*

depend-graph:
	@echo "from motorise import Agent; agent = Agent()" > temp.py
	@pycallgraph --include "motorise*" graphviz --output-file=depend.png -- temp.py
	@rm temp.py
