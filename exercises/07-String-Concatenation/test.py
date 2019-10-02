import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os


@pytest.mark.it("1. You should create a variable named my_var1")
def test_use_my_var1():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("my_var1") > 0
@pytest.mark.it("2. You should create a variable named my_var2")
def test_use_my_var2():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("my_var2") > 0
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