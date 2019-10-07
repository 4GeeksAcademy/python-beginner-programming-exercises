# from app import my_function
import pytest,os,re,io,sys, mock, json

@pytest.mark.it("1. The console should return the correct string for each condition")
def test_t(stdin):
    _input = json.loads(stdin)
    print("####", _input)
    with mock.patch('builtins.input', lambda x: _input[0]):
        if int(_input[0]) > 100:
            # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
            sys.stdout = buffer = io.StringIO()
            import app

            assert "Give me your money!\n" == buffer.getvalue()
        elif int(_input[0]) < 100 and int(_input[0]) > 50:
            sys.stdout = buffer = io.StringIO()
            import app

            assert "Buy me some coffee you cheap!\n" == buffer.getvalue()
        elif int(_input[0]) < 50:
            sys.stdout = buffer = io.StringIO()
            import app

            assert "You are a poor guy, go away!\n" == buffer.getvalue()




