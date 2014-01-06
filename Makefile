.PHONY: clean clean-pyc test test-env create-dist

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
	@venv/bin/py.test tests

test-env:
	@virtualenv-2.7 --no-site-package venv
	@venv/bin/pip install -r requirements.txt

create-dist: clean
	@python setup.py sdist

upload-dist:
	@python setup.py sdist upload

depend-graph:
	@echo "from motorise import Agent; agent = Agent()" > temp.py
	@pycallgraph --include "motorise*" graphviz --output-file=depend.png -- temp.py
	@rm temp.py
