import argparse


def generate_diff(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        diff_file1 = dict(sorted(json.load(f1).items()))
        diff_file2 = dict(sorted(json.load(f2).items()))
        out = ''
        diff_key = diff_file2.keys() - diff_file1.keys()
        for key, value in diff_file1.items():
            if value == diff_file2.get(key):
                out = f'{out}   {key}: {value}\n'
            elif diff_file2.get(key) == None:
                out = f'{out} - {key}: {value}\n'
            elif value != diff_file2.get(key):
                out = f'{out} - {key}: {value}\n'
                out = f'{out} + {key}: {diff_file2.get(key)}\n' 
        for key in diff_key:
            if diff_file1.get(key) == None:
                out = f'{out} + {key}: {diff_file2.get(key)}\n'
                
    return f'{{\n{out}}}'