import yaml
from jinja2 import Template, Environment, FileSystemLoader

test = yaml.load(open("test.yaml"))
env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('test.ji')

template.render(test)

