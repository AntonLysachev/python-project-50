from gendiff.generator import generate_diff
import pytest
import os


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


def build_fixture_path(file_name):
    return os.path.join(FIXTURES_PATH, file_name)


def get_content(file_name):
    addres = build_fixture_path(file_name)
    with open(addres, 'r') as f:
        data = f.read()
    return data


@pytest.mark.parametrize("file_path1,file_path2,style,file_name", [
    ('file_json1.json',
     'file_json2.json',
     'stylish', 'expected.txt'),
    ('file_yaml1.yml',
     'file_yaml2.yml',
     'stylish', 'expected.txt'),
    ('file_yaml1.yml',
     'file_json2.json',
     'stylish', 'expected.txt'),
    ('file_json3.json',
     'file_json4.json',
     'stylish', 'expected_empty_files.txt'),
    ('file_json3.json',
     'file_json1.json',
     'stylish', 'expected_empty_one_file.txt'),
    ('file_json1.json',
     'file_json3.json',
     'stylish', 'expected_empty_tow_file.txt'),
    ('file_json5.json',
     'file_json6.json',
     'stylish', 'expected_tree.txt'),
    ('file_json5.json',
     'file_json6.json',
     'plain', 'expected_tree_plain.txt'),
    ('file_json1.json',
     'file_json2.json',
     'plain', 'expected_plain.txt'),
    ('file_json3.json',
     'file_json1.json',
     'plain', 'expected_empty_one_file_plain.txt'),
    ('file_json1.json',
     'file_json3.json',
     'plain', 'expected_empty_tow_file_plain.txt'),
    ('file_json5.json',
     'file_json6.json',
     'json', 'expected_tree_json.txt'),
    ('file_json.txt',
     'file_yaml.txt',
     'stylish', 'expected_Unknown_format.txt'),
    ('file_json1.json',
     'file_json2.json',
     'stylis', 'expected_Invalid_format_entered.txt'),])
def test_generate_diff(file_path1, file_path2, style, file_name):
    answer = get_content(file_name)
    path1 = build_fixture_path(file_path1)
    path2 = build_fixture_path(file_path2)
    assert generate_diff(path1, path2, style) == answer
