import json
import yaml
import os


# Для чего нам разделять на 2 функции
# почему не оставить все в одной
def parse(content, format):
    if format == '.json':
        return json.load(content)
    if format in ('.yml', '.yaml'):
        return yaml.full_load(content)
    raise Exception('Unknown extension')


def get_data(addres):
    _, extension = os.path.splitext(addres)
    with open(addres, "r") as content:
        return parse(content, extension)
