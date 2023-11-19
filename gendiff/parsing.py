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


def parsing(date1, date2):
    analyzed = {}
    for key, value in date1.items():
        value = to_json_style(value)
        value2 = to_json_style(date2.get(key, 'empty'))
        analyzed.update({key: {}})
        if isinstance(value, dict):
            if isinstance(value2, dict):
                analyzed[key].update({'children':
                                      parsing(date1[key], date2[key])})
            else:
                analyzed[key].update({'value1': value, 'value2': value2})
        else:
            analyzed[key].update({'value1': value, 'value2': value2})
    for key, value in date2.items():
        value = to_json_style(value)
        value1 = to_json_style(date1.get(key, 'empty'))
        if value1 == 'empty':
            analyzed.update({key: {'value1': value1, 'value2': value}})
    return dict(sorted(analyzed.items()))
