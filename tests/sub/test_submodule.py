
def test_sub(datafix):
    filecontents = datafix.read_text()
    assert filecontents == '12\n'
