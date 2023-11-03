def parsing(date1, date2):
    analyzed = {}
    for key in date1.keys():
        if date1[key] == date2.get(key):
            analyzed.update({key: f'  {key}: {date1[key]}'})
        else:
            analyzed.update({key: f'- {key}: {date1[key]}'})
    for key in date2.keys():
        if date2[key] != date1.get(key):
            analyzed.update({f'{key}2': f'+ {key}: {date2[key]}'})
    return dict(sorted(analyzed .items()))
