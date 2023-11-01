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
    assert generate_diff('test/fixtures/file1.json', 
                         'test/fixtures/file2.json') == answer1
    

def test_generate_diff_empty_files():
    assert generate_diff('test/fixtures/file3.json', 
                         'test/fixtures/file4.json') == answer2


def test_generate_diff_empty_one_file():
    assert generate_diff('test/fixtures/file3.json', 
                         'test/fixtures/file1.json') == answer3
    

def test_generate_diff_empty_tow_file():
    assert generate_diff('test/fixtures/file1.json', 
                         'test/fixtures/file3.json') == answer4