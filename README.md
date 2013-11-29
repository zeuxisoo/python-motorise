### Installation

Create virtualenv

	virtualenv --no-site-package venv
	
Activate virtuleenv
	
	source venv/bin/activate
	
Install the motorise
	
	pip install motorise
	
### Usage

Simple

	from motorise import Agent
	
	agent = Agent()
	page  = agent.get("http://www.google.com/")
	
	print(page.title())