import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re


@pytest.mark.it("1. You should create a variable named my_var1")
def test_use_my_var1():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_var1 = [s for s in content if "my_var1" in s]
    my_var1Var = content.index(my_var1[0])
    regex_my_var1 = r"my_var1(\s*)=(\s*)\"(\s*)Hello(\s*)\""
    # regex = r"color = \"red\""
    # regex = r"color(\s*)=(\s*)\"red\""
    assert re.match(regex_my_var1, content[my_var1Var])
@pytest.mark.it("2. You should create a variable named my_var2")
def test_use_my_var2():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_var2 = [s for s in content if "my_var2" in s]
    my_var2Var = content.index(my_var2[0])
    regex_my_var2 = r"my_var2(\s*)=(\s*)\"(\s*)World(\s*)\""
    # regex = r"color = \"red\""
    # regex = r"color(\s*)=(\s*)\"red\""
    assert re.match(regex_my_var2, content[my_var2Var])
@pytest.mark.it('3. Your code needs to print Hello World on the console')
def test_for_file_output(capsys):

    captured = buffer.getvalue()
    assert captured == "Hello World\n" #add \n because the console jumps the line on every print

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True