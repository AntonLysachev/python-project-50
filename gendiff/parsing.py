def parsing(date1, date2):
    def analyz(date1, date2):
        analyzed = {}
        for key, value in date1.items():
            analyzed.update({key: {}})
            if isinstance(value, dict):
                if isinstance(date2.get(key), dict):
                    analyzed[key].update({'children': analyz(date1[key], date2[key])})
                else:
                    analyzed[key].update({'value1': value, 'value2': date2.get(key)})
            else:
                analyzed[key].update({'value1': value, 'value2': date2.get(key)})
        for key, value in date2.items():
            if date1.get(key) == None:
                analyzed.update({key: {'value1': date1.get(key), 'value2': value}})
        return dict(sorted(analyzed.items()))
    return analyz(date1, date2)
