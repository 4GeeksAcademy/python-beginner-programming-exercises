import pytest,os,re,io,sys, mock, json

@pytest.mark.it("Print on the console the input value + 10")
def test_t(stdin):
    _input = json.loads(stdin)
    my_testString = int(_input[0]) + 10
    with mock.patch('builtins.input', lambda x: _input.pop()):
      # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
      sys.stdout = buffer = io.StringIO()
      import app
      captured = buffer.getvalue()
      assert captured == "Your age is: " + str(my_testString)+'\n'
