#!/usr/bin/python
import json
from jinja2 import Template, Environment, FileSystemLoader

test = json.load(open("test.json"))
env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('site.pp.jinja')

print template.render(test)

