from gendiff.generate_diff import generate_diff
import pytest


def get_answer(posrfix):
    addres = f'test/fixtures/answer/test_generate_diff{posrfix}'
    with open(addres, 'r') as f:
        data = f.read()
    return data


@pytest.mark.parametrize("file_path1,file_path2,style,posrfix", [
    ('test/fixtures/file_json1.json',
     'test/fixtures/file_json2.json',
     'stylish', '.txt'),
    ('test/fixtures/file_yaml1.yml',
     'test/fixtures/file_yaml2.yml',
     'stylish', '.txt'),
    ('test/fixtures/file_yaml1.yml',
     'test/fixtures/file_json2.json',
     'stylish', '.txt'),
    ('test/fixtures/file_json3.json',
     'test/fixtures/file_json4.json',
     'stylish', '_empty_files.txt'),
    ('test/fixtures/file_json3.json',
     'test/fixtures/file_json1.json',
     'stylish', '_empty_one_file.txt'),
    ('test/fixtures/file_json1.json',
     'test/fixtures/file_json3.json',
     'stylish', '_empty_tow_file.txt'),
    ('test/fixtures/file_json5.json',
     'test/fixtures/file_json6.json',
     'stylish', '_tree.txt'),
    ('test/fixtures/file_json5.json',
     'test/fixtures/file_json6.json',
     'plain', '_plain.txt'),
    ('test/fixtures/file_json5.json',
     'test/fixtures/file_json6.json',
     'json', '_tree_json.txt'),
    ('test/fixtures/file_json.txt',
     'test/fixtures/file_yaml.txt',
     'stylish', '_Unknown_format.txt'),])
def test_generate_diff(file_path1, file_path2, style, posrfix):
    answer = get_answer(posrfix)
    assert generate_diff(file_path1, file_path2, style) == answer
