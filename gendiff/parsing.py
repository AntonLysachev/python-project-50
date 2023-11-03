def parsing(date1, date2):
    analyzed = {}
    for key, value in date1.items():
        if value == date2.get(key):
            prefix = ' '
        else:
            prefix = '-'
        analyzed.update({key: f'{prefix} {key}: {value}'})
    for key, value in date2.items():
        if value != date1.get(key):
            analyzed.update({f'{key}2': f'+ {key}: {value}'})
    return dict(sorted(analyzed .items()))
