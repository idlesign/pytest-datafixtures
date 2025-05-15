

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

    strio = datafix_read('test_datafix.txt', encoding='utf-8', io=True)
    assert strio.read() == 'testit\n'


def test_datafix_readbin(datafix_readbin):
    filecontents = datafix_readbin('fileone')
    assert filecontents[0] == 208

    binio = datafix_readbin('fileone', io=True)
    assert binio.read(1) == b'\xd0'


def test_datafix_dump(datafix_dump, datafix_read, datafix_readbin):

    # default naming
    assert f"{datafix_dump('sometext')}".endswith('test_datafix_dump')
    assert datafix_read() == 'sometext'

    # custom naming
    assert f"{datafix_dump('moretext', 'myfile.txt')}".endswith('myfile.txt')
    assert datafix_read('myfile.txt') == 'moretext'

    # binary
    assert datafix_dump(b'somebin', 'mybin.bin')
    assert datafix_readbin('mybin.bin') == b'somebin'
