import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re

@pytest.mark.it("1. You should create a variable named color")
def test_use_forLoop():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]

    # regex = r"color = \"red\""
    regex = r"color(\s*)=(\s*)\"red\""
    assert re.match(regex, content[0])
@pytest.mark.it('2. You should print on the console the value red ')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert captured == "red\n" #add \n because the console jumps the line on every print
# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True