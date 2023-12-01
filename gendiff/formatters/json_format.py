import json


def form_json(parsing_file):
    return json.dumps(parsing_file, indent=2)
