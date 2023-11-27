def to_json_style(value):
    match value:
        case None:
            return 'null'
        case False:
            return 'false'
        case True:
            return 'true'
        case _:
            return value


def parsing(data1, data2):
    analyzed = {}
    for key, value in data1.items():
        value = to_json_style(value)
        value2 = to_json_style(data2.get(key, 'empty'))
        analyzed.update({key: {}})
        if isinstance(value, dict):
            if isinstance(value2, dict):
                analyzed[key].update({'children':
                                      parsing(data1[key], data2[key])})
            else:
                analyzed[key].update({'value1': value, 'value2': value2})
        else:
            analyzed[key].update({'value1': value, 'value2': value2})
    for key, value in data2.items():
        value = to_json_style(value)
        value1 = to_json_style(data1.get(key, 'empty'))
        if value1 == 'empty':
            analyzed.update({key: {'value1': value1, 'value2': value}})
    return dict(sorted(analyzed.items()))
