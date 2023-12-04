import json
import yaml
import os


def get_data(addres):
    _, extension = os.path.splitext(addres)
    if extension == '.json':
        with open(addres, "r") as f:
            return json.load(f)
    if extension in ('.yml', '.yaml'):
        with open(addres, "r") as f:
            return yaml.full_load(f)
    raise Exception('Unknown extension')
