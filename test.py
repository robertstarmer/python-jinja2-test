#!/usr/bin/python
import yaml
from jinja2 import Template, Environment, FileSystemLoader

test = yaml.load(open("test.json"))
env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('site.pp.jinja')

print template.render(test)

