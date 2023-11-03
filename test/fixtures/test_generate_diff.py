from gendiff.generate_diff import generate_diff

def get_answer(file):
    with open (file, 'r') as f:
        data = f.read()
    return data

answer1 = get_answer('test/fixtures/answer/test_generate_diff.txt')
answer2 = get_answer('test/fixtures/answer/test_generate_diff_empty_files.txt')
answer3 = get_answer('test/fixtures/answer/test_generate_diff_empty_one_file.txt')
answer4 = get_answer('test/fixtures/answer/test_generate_diff_empty_tow_file.txt')

def test_generate_diff():
    assert generate_diff('test/fixtures/file_json1.json', 
                         'test/fixtures/file_json2.json') == answer1
    

def test_generate_diff_empty_files():
    assert generate_diff('test/fixtures/file_json3.json', 
                         'test/fixtures/file_json4.json') == answer2


def test_generate_diff_empty_one_file():
    assert generate_diff('test/fixtures/file_json3.json', 
                         'test/fixtures/file_json1.json') == answer3
    

def test_generate_diff_empty_tow_file():
    assert generate_diff('test/fixtures/file_json1.json', 
                         'test/fixtures/file_json3.json') == answer4


def test_generate_diff_yaml():
    assert generate_diff('test/fixtures/file_yaml1.yml', 
                         'test/fixtures/file_yaml2.yml') == answer1
    

def test_generate_diff_empty_files_yaml():
    assert generate_diff('test/fixtures/file_yaml3.yml', 
                         'test/fixtures/file_yaml4.yml') == answer2


def test_generate_diff_empty_one_file_yaml():
    assert generate_diff('test/fixtures/file_yaml3.yml', 
                         'test/fixtures/file_yaml1.yml') == answer3
    

def test_generate_diff_empty_tow_file_yaml():
    assert generate_diff('test/fixtures/file_yaml1.yml', 
                         'test/fixtures/file_yaml3.yml') == answer4
    

def test_generate_diff_yaml_json():
    assert generate_diff('test/fixtures/file_yaml1.yml', 
                         'test/fixtures/file_json2.json') == answer1
    

def test_generate_diff_empty_files_yaml_json():
    assert generate_diff('test/fixtures/file_yaml3.yml', 
                         'test/fixtures/file_json4.json') == answer2


def test_generate_diff_empty_one_file_yaml_json():
    assert generate_diff('test/fixtures/file_yaml3.yml', 
                         'test/fixtures/file_json1.json') == answer3
    

def test_generate_diff_empty_tow_file_yaml_json():
    assert generate_diff('test/fixtures/file_yaml1.yml',
                         'test/fixtures/file_json3.json') == answer4
    

def test_generate_diff_unknown_format():
    assert generate_diff('test/fixtures/file_yaml1.yml',
                         'test/fixtures/file_yaml2.txt') == 'Unknown format'