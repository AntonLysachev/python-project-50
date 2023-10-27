from gendiff.generate_diff import generate_diff


def test_generate_diff():
    assert generate_diff('test/fixtures/file1.json', 
                         'test/fixtures/file2.json') == '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'
    

def test_generate_diff_empty_files():
    assert generate_diff('test/fixtures/file3.json', 
                         'test/fixtures/file4.json') == "{\n}"


def test_generate_diff_empty_one_file():
    assert generate_diff('test/fixtures/file3.json', 
                         'test/fixtures/file1.json') == '{\n + follow: False\n + host: hexlet.io\n + proxy: 123.234.53.22\n + timeout: 50\n}'
    

def test_generate_diff_empty_tow_file():
    assert generate_diff('test/fixtures/file1.json', 
                         'test/fixtures/file3.json') == '{\n - follow: False\n - host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n}'