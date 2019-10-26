### Status

[![Build Status](https://travis-ci.org/zeuxisoo/python-motorise.png?branch=master)](https://travis-ci.org/zeuxisoo/python-motorise)

### Installation

Create virtualenv

	python3 -m venv venv3

Activate virtuleenv

	source venv3/bin/activate

Install the motorise

	pip install motorise

### Usage

Sample 1

	from motorise import Agent

	agent = Agent()
	page  = agent.get("http://www.google.com/")

	print(page.title())

Sample 2

	from motorise import Agent

	agent = Agent()
	page  = agent.get("http://www.google.com/")
	form  = page.form("form[name=f]")
	form.set_field('q', 'github')
	submit = agent.submit(form)

	print([(link.href(), link.text()) for link in submit.links()])
