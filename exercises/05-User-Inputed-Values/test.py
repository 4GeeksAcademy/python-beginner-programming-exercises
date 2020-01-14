import pytest,os,re,io,sys, mock, json

@pytest.mark.it("We tried with age 50 and it was supposed to return 60")
def test_t(stdin):
    with mock.patch('builtins.input', lambda x: 50):
      # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
      sys.stdout = buffer = io.StringIO()
      import app
      captured = buffer.getvalue()
      assert captured == "Your age is: 60\n"
