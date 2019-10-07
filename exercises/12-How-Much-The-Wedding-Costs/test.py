# from app import my_function
import pytest,os,re,io,sys, mock, json

@pytest.mark.it("1. The console should return the correct string for each condition")
def test_t(stdin):
    _input = json.loads(stdin)
    print("####", _input)
    with mock.patch('builtins.input', lambda x: _input[0]):
        if int(_input[0]) > 100 and int(_input[0]) < 200:
            # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
            sys.stdout = buffer = io.StringIO()
            import app
            price = 15000

            "Your wedding will cost "+str(price)+" dollars\n" == buffer.getvalue()
        elif int(_input[0]) < 101 and int(_input[0]) > 50:
            sys.stdout = buffer = io.StringIO()
            import app
            price = 10000

            assert "Your wedding will cost "+str(price)+" dollars\n" == buffer.getvalue()
        elif int(_input[0]) < 50:
            sys.stdout = buffer = io.StringIO()
            import app
            price = 4000
            "Your wedding will cost "+str(price)+" dollars\n" == buffer.getvalue()
        elif int(_input[0]) > 200:
            sys.stdout = buffer = io.StringIO()
            import app
            price = 20000
            "Your wedding will cost "+str(price)+" dollars\n" == buffer.getvalue()
