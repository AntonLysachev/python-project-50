def define(file):
    format = file.split('.')
    match format:
        case _, 'yaml' | 'yml':
            return 'yml'
        case _, 'json':
            return 'json'
        case _:
            return False
