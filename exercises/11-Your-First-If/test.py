# from app import my_function
import pytest,os,re,io,sys, mock, json

@pytest.mark.it('Use the function print()')
def test_for_print():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\(.+\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Test for more than 100")
def test_for_more(stdin):
    _input = json.loads(stdin)
    with mock.patch('builtins.input', lambda x: 101):
        sys.stdout = buffer = io.StringIO()
        import app
        assert "Give me your money!\n" == buffer.getvalue()

@pytest.mark.it("Test for exactly 100 should be: Buy me some coffee you cheap ")
def test_between(stdin):
    _input = json.loads(stdin)
    with mock.patch('builtins.input', lambda x: 100):
        sys.stdout = buffer = io.StringIO()
        import app
        assert "Buy me some coffee you cheap!\n" == buffer.getvalue()

@pytest.mark.it("Test for exactly 50 should be: You are a poor guy, go away")
def test_for_less(stdin):
    with mock.patch('builtins.input', lambda x: 50):
        sys.stdout = buffer = io.StringIO()
        import app
        assert "You are a poor guy, go away!\n" == buffer.getvalue()




