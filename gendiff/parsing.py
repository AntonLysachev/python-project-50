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


def nested(value):
    nested_key = {}
    if isinstance(value, dict):
        for key, value_in in value.items():
            nested_key.update({key: {}})
            nested_key[key].update({'type': 'nested'})
            if isinstance(value_in, dict):
                nested_key[key].update({'value': nested(value_in)})
            else:
                nested_key[key].update({'value': value_in})
        return nested_key
    return value


def add_data(value1, value2):
    data = {}
    if value1 != value2 and value1 != 'empty' and value2 != 'empty':
        data.update({'type': 'updated',
                     'old_value': nested(value1),
                     'new_value': nested(value2)})
    if value1 == 'empty':
        data.update({'type': 'added', 'value': nested(value2)})
    if value2 == 'empty':
        data.update({'type': 'removed', 'value': nested(value1)})
    if value1 == value2:
        data.update({'type': 'not updated', 'value': nested(value1)})
    return data



def parsing(date1, date2):
    analyzed = {}
    for key, value in date1.items():
        value1 = to_json_style(value)
        value2 = to_json_style(date2.get(key, 'empty'))
        analyzed.update({key: {}})
        if isinstance(value1, dict):
            if isinstance(value2, dict):
                analyzed[key].update({'children': 
                                      parsing(date1[key], date2[key])})
            else:
                analyzed[key].update(add_data(value1, value2))
        else:
            analyzed[key].update(add_data(value1, value2))
    for key, value in date2.items():
        value2 = to_json_style(value)
        value1 = to_json_style(date1.get(key, 'empty'))
        if value1 == 'empty':
            analyzed.update({key: add_data(value1, value2)})
    return dict(sorted(analyzed.items()))
# def to_json_style(value):
#     match value:
#         case None:
#             return 'null'
#         case False:
#             return 'false'
#         case True:
#             return 'true'
#         case _:
#             return value


# def parsing(data1, data2):
#     analyzed = {}
#     for key, value in data1.items():
#         value = to_json_style(value)
#         value2 = to_json_style(data2.get(key, 'empty'))
#         analyzed.update({key: {}})
#         if isinstance(value, dict):
#             if isinstance(value2, dict):
#                 analyzed[key].update({'children':
#                                       parsing(data1[key], data2[key])})
#             else:
#                 analyzed[key].update({'value1': value, 'value2': value2})
#         else:
#             analyzed[key].update({'value1': value, 'value2': value2})
#     for key, value in data2.items():
#         value = to_json_style(value)
#         value1 = to_json_style(data1.get(key, 'empty'))
#         if value1 == 'empty':
#             analyzed.update({key: {'value1': value1, 'value2': value}})
#     return dict(sorted(analyzed.items()))
