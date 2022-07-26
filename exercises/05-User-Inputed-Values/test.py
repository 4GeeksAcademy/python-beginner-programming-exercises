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
    assert captured == "Your age is: 60\n"

@pytest.mark.it('There should be a variable named age')
def test_variable_exists():
    try:
        import app
        app.age
    except AttributeError:
        raise AttributeError('The variable "age" should exist on app.py')