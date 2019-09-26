# from app import my_function
import pytest,os,re,io,sys, mock, json

@pytest.mark.it("1. You should not delete or change the existing code")
def test_t(stdin):
    _input = json.loads(stdin)
    print("####", _input)
    with mock.patch('builtins.input', lambda x: _input.pop()):
      # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
      sys.stdout = buffer = io.StringIO()
      import app
      # content = f.readlines()
      # regex = r"total = int\(input\('How much money do you have in your pocket\?'\)\)"
      # assert re.match(regex, content[0])
      assert "Give me your money!\n" == buffer.getvalue()
# @pytest.mark.it("2. You should not delete or change the existing code")
# def test_e(stdin):
#     _input = json.loads(stdin)
#     with mock.patch('builtins.input', lambda x: _input.pop()):
#       # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
#       sys.stdout = buffer = io.StringIO()
#       import app
#       # content = f.readlines()
#       # regex = r"total = int\(input\('How much money do you have in your pocket\?'\)\)"
#       # assert re.match(regex, content[0])
#       assert "Buy me some coffee you cheap!\n" == buffer.getvalue()
# @pytest.mark.it("3. You should not delete or change the existing code")
# def test_w(stdin):
#     _input = json.loads(stdin)
#     with mock.patch('builtins.input', lambda x: _input.pop()):
#       # f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
#       sys.stdout = buffer = io.StringIO()
#       import app
#       # content = f.readlines()
#       # regex = r"total = int\(input\('How much money do you have in your pocket\?'\)\)"
#       # assert re.match(regex, content[0])
#       assert "You are a poor guy, go away!\n" == buffer.getvalue()

# @pytest.mark.it('Your code needs to print hello on the console')
# def test_for_file_output(capsys):
#     regex = r"print\(random\.rand(\w+)\(10\)\) "
#     captured = buffer.getvalue()
#     assert captured == regex #add \n because the console jumps the line on every print

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True