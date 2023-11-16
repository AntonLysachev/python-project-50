import json
import yaml


def define(file):
    format = file.split('.')
    match format:
        case _, 'yaml' | 'yml':
            return 'yml'
        case _, 'json':
            return 'json'
        case _:
            return False


def get_date(file):
    format = define(file)
    if format == 'json':
        with open(file, "r") as f:
            return json.load(f)
    if format == 'yml':
        with open(file, "r") as f:
            return yaml.full_load(f)
