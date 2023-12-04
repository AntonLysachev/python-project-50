from gendiff.generate_diff_tree import generate_diff
import pytest
import os


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


def build_fixture_path(file_name):
    return os.path.join(FIXTURES_PATH, file_name)


def get_content(addres):
    with open(addres, 'r') as f:
        data = f.read()
        return data


@pytest.mark.parametrize("file_path1,file_path2,style,file_name", [
    ('file_json1.json',
     'file_json2.json',
     'stylish', 
     'test/fixtures/expected.txt'),
    ('file_yaml1.yml',
     'file_yaml2.yml',
     'stylish', 
     'test/fixtures/expected.txt'),
    ('file_yaml1.yml',
     'file_json2.json',
     'stylish', 
     'test/fixtures/expected.txt'),
    ('file_json3.json',
     'file_json4.json',
     'stylish', 
     'test/fixtures/expected_empty_files.txt'),
    ('file_json3.json',
     'file_json1.json',
     'stylish', 
     'test/fixtures/expected_empty_one_file.txt'),
    ('file_json1.json',
     'file_json3.json',
     'stylish', 
     'test/fixtures/expected_empty_tow_file.txt'),
    ('file_json5.json',
     'file_json6.json',
     'stylish', 
     'test/fixtures/expected_tree.txt'),
    ('file_json5.json',
     'file_json6.json',
     'plain', 
     'test/fixtures/expected_tree_plain.txt'),
    ('file_json1.json',
     'file_json2.json',
     'plain', 'test/fixtures/expected_plain.txt'),
    ('file_json3.json',
     'file_json1.json',
     'plain', 
     'test/fixtures/expected_empty_one_file_plain.txt'),
    ('file_json1.json',
     'file_json3.json',
     'plain', 
     'test/fixtures/expected_empty_tow_file_plain.txt'),
    ('file_json5.json',
     'file_json6.json',
     'json', 
     'test/fixtures/expected_tree_json.txt'),
     ('file_json1.json',
      'file_json2.json',
      'stylis', 
      'Invalid'),
      ('file_json.txt',
       'file_yaml.txt',
       'stylis', 
       'Unknown')])
def test_generate_diff(file_path1, file_path2, style, file_name):
    path1 = build_fixture_path(file_path1)
    path2 = build_fixture_path(file_path2)
    if file_name == 'Invalid':
        with pytest.raises(Exception) as exception:
            generate_diff(path1, path2, style)
        assert str(exception.value) == 'Invalid format entered'
    elif file_name == 'Unknown':
        with pytest.raises(Exception) as exception:
            generate_diff(path1, path2)
        assert str(exception.value) == 'Unknown extension'
    else:
        answer = get_content(file_name)
        assert generate_diff(path1, path2, style) == answer
