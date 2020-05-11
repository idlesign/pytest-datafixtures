

def test_datafix_dir(datafix_dir):

    assert datafix_dir.exists()
    assert f'{datafix_dir}'.endswith('/tests/datafixtures')

    files = list(f'{file.name}' for file in datafix_dir.iterdir())
    assert 'fileone' in files

    file = datafix_dir / 'fileone'

    filecontent = file.read_text()
    assert filecontent == 'Раздватричетырепять\n'

    filecontent = file.read_bytes()
    assert filecontent[0] == 208


def test_datafix(datafix):
    filecontents = datafix.with_suffix('.txt').read_text()
    assert filecontents == 'testit\n'


def test_datafix_read(datafix_read):
    filecontents = datafix_read('test_datafix.txt')
    assert filecontents == 'testit\n'
