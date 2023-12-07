import json
import yaml
import os


def parse(content, format):
    if format == '.json':
        return json.load(content)
    if format in ('.yml', '.yaml'):
        return yaml.full_load(content)
    raise ValueError('Unknown extension')


def get_data(addres):
    _, extension = os.path.splitext(addres)
    with open(addres, "r") as content:
        return parse(content, extension)
