def to_null(value):
    if value is None:
        return 'null'
    return value


def parsing(date1, date2):
    def analyz(date1, date2):
        analyzed = {}
        for key, value in date1.items():
            value = to_null(value)
            value2 = to_null(date2.get(key, 'empty'))
            analyzed.update({key: {}})
            if isinstance(value, dict):
                if isinstance(value2, dict):
                    analyzed[key].update({'children':
                                          analyz(date1[key], date2[key])})
                else:
                    analyzed[key].update({'value1': value, 'value2': value2})
            else:
                analyzed[key].update({'value1': value, 'value2': value2})
        for key, value in date2.items():
            value = to_null(value)
            value1 = to_null(date1.get(key, 'empty'))
            if value1 == 'empty':
                analyzed.update({key: {'value1': value1, 'value2': value}})
        return dict(sorted(analyzed.items()))
    return analyz(date1, date2)
