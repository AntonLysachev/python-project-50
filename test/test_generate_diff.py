from gendiff.generator import generate_diff
import pytest


def get_answer(file_name):
    addres = f'test/fixtures/expected{file_name}'
    with open(addres, 'r') as f:
        data = f.read()
    return data


def get_addres(file_path):
    return f'test/fixtures/file_{file_path}'


@pytest.mark.parametrize("file_path1,file_path2,style,file_name", [
    ('json1.json',
     'json2.json',
     'stylish', '.txt'),
    ('yaml1.yml',
     'yaml2.yml',
     'stylish', '.txt'),
    ('yaml1.yml',
     'json2.json',
     'stylish', '.txt'),
    ('json3.json',
     'json4.json',
     'stylish', '_empty_files.txt'),
    ('json3.json',
     'json1.json',
     'stylish', '_empty_one_file.txt'),
    ('json1.json',
     'json3.json',
     'stylish', '_empty_tow_file.txt'),
    ('json5.json',
     'json6.json',
     'stylish', '_tree.txt'),
    ('json5.json',
     'json6.json',
     'plain', '_plain.txt'),
    ('json5.json',
     'json6.json',
     'json', '_tree_json.txt'),
    ('json.txt',
     'yaml.txt',
     'stylish', '_Unknown_format.txt'),])
def test_generate_diff(file_path1, file_path2, style, file_name):
    answer = get_answer(file_name)
    path1 = get_addres(file_path1)
    path2 = get_addres(file_path2)
    assert generate_diff(path1, path2, style) == answer
