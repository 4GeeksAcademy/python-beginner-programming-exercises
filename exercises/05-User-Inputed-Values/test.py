import pytest,os,re,io,sys,mock,json
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('Use the function print()')
def test_for_file_output(capsys):
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = (r"print\s*\(")
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True

@pytest.mark.it("We tried with age 50 and it was supposed to return 60")
@mock.patch('builtins.input', lambda x: 50)
def test_plus_ten(stdin):
    # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    sys.stdout = buffer = io.StringIO()
    import app
    captured = buffer.getvalue()
    assert   "Your age is: 60\n" in captured
    
