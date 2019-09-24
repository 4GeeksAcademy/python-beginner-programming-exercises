import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app

@pytest.mark.it("1. You should create a function called generate_random")
def test_use_my_var1():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("def generate_random():") > 0
@pytest.mark.it("2. You should print a random integer inside generate_random function")
def test_use_print():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("print") > 0
@pytest.mark.it("3. You should call generate_random function correctly")
def test_call_generate_random():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("generate_random()") > 0
# @pytest.mark.it('Your code needs to print hello on the console')
# def test_generate_random(capsys):
#     x = get_generate_random()
#     print("x", x)
#     captured = buffer.getvalue()
#     assert captured == "hello\n" #add \n because the console jumps the line on every print

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True