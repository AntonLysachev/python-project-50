from gendiff.generate_diff import generate_diff


def get_answer(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


answer1 = get_answer('test/fixtures/answer/test_generate_diff.txt')
answer2 = get_answer('test/fixtures/answer/test_generate_diff_empty_files.txt')
answer3 = get_answer('test/fixtures/answer/test_generate_diff_empty_one_file.txt')
answer4 = get_answer('test/fixtures/answer/test_generate_diff_empty_tow_file.txt')
answer5 = get_answer('test/fixtures/answer/test_generate_diff_tree.txt')
answer6 = get_answer('test/fixtures/answer/test_generate_diff_plain.txt')
answer7 = get_answer('test/fixtures/answer/json/test_generate_diff.txt')
answer8 = get_answer('test/fixtures/answer/json/test_generate_diff_empty_files.txt')
answer9 = get_answer('test/fixtures/answer/json/test_generate_diff_empty_one_file.txt')
answer10 = get_answer('test/fixtures/answer/json/test_generate_diff_empty_tow_file.txt')
answer11 = get_answer('test/fixtures/answer/json/test_generate_diff_tree.txt')


def test_generate_diff():
    assert generate_diff('test/fixtures/file_json1.json',
                         'test/fixtures/file_json2.json',
                         'stylish') == answer1


def test_generate_diff_empty_files():
    assert generate_diff('test/fixtures/file_json3.json',
                         'test/fixtures/file_json4.json',
                         'stylish') == answer2


def test_generate_diff_empty_one_file():
    assert generate_diff('test/fixtures/file_json3.json',
                         'test/fixtures/file_json1.json',
                         'stylish') == answer3


def test_generate_diff_empty_tow_file():
    assert generate_diff('test/fixtures/file_json1.json',
                         'test/fixtures/file_json3.json',
                         'stylish') == answer4


def test_generate_diff_yaml():
    assert generate_diff('test/fixtures/file_yaml1.yml',
                         'test/fixtures/file_yaml2.yml',
                         'stylish') == answer1


def test_generate_diff_yaml_json():
    assert generate_diff('test/fixtures/file_yaml1.yml',
                         'test/fixtures/file_json2.json',
                         'stylish') == answer1


def test_generate_diff_tree():
    assert generate_diff('test/fixtures/file_json5.json',
                         'test/fixtures/file_json6.json',
                         'stylish') == answer5


def test_generate_diff_plain():
    assert generate_diff('test/fixtures/file_json5.json',
                         'test/fixtures/file_json6.json',
                         'plain') == answer6


def test_generate_diff_unknown_format():
    assert generate_diff('test/fixtures/file_json.txt',
                         'test/fixtures/file_yaml.txt',
                         'stylish') == 'Unknown format'


def test_generate_diff_json():
    assert generate_diff('test/fixtures/file_json1.json',
                         'test/fixtures/file_json2.json',
                         'json') == answer7


def test_generate_diff_json_empty_files():
    assert generate_diff('test/fixtures/file_json3.json',
                         'test/fixtures/file_json4.json',
                         'json') == answer8


def test_generate_diff_json_empty_one_file():
    assert generate_diff('test/fixtures/file_json3.json',
                         'test/fixtures/file_json1.json',
                         'json') == answer9


def test_generate_diff_json_empty_tow_file():
    assert generate_diff('test/fixtures/file_json1.json',
                         'test/fixtures/file_json3.json',
                         'json') == answer10


def test_generate_diff_json_tree():
    assert generate_diff('test/fixtures/file_json5.json',
                         'test/fixtures/file_json6.json',
                         'json') == answer11
