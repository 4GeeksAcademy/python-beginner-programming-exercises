import io
import sys
sys.stdin.buffer.read()
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re



@pytest.mark.it("1. You should not delete or change the existing code")
def test_existing_code():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    regex = r"total = int\(input\('How much money do you have in your pocket\?'\)\)"
    assert re.match(regex, content[0])
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