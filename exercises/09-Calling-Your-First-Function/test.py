import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re
# @pytest.mark.it('Your code needs to print hello on the console')
# def test_for_file_output(capsys):
#     captured = buffer.getvalue()
#     assert captured == "hello\n" #add \n because the console jumps the line on every print
@pytest.mark.it("1. You should call is_odd function in your print statement and pass the value 45345")
def test_conditional():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "print" in s]
    my_printVar = content.index(my_print[0])
    regex = r"print\(is_odd\(45345\)\)"
    assert re.match(regex, content[my_printVar])

@pytest.mark.it('2. The console should return True ')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert captured == "True\n"
# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True