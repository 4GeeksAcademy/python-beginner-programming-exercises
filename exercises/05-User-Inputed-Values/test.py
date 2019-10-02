import pytest,os,re,io,sys, mock, json

@pytest.mark.it("1. You should print on the console the input value + 10")
def test_t(stdin):
    _input = json.loads(stdin)
    print("####", _input[0])
    my_testString = int(_input[0]) + 10
    print("$$$$$:",int(my_testString) + 10)
    with mock.patch('builtins.input', lambda x: _input.pop()):
      # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
      sys.stdout = buffer = io.StringIO()
      import app
      captured = buffer.getvalue()
      assert captured == "Your age is: " + str(my_testString)+'\n'
