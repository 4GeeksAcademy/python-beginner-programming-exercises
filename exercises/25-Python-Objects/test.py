import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re

@pytest.mark.it("1. You should not delete or change the existing code")
def test_existing_code():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    print("@@@@",content)

    original_input = [
        r"class Person:",
	      r"(\s*)name = \"John\"",
	      r"(\s*)lastname = \"Doe\"",
	      r"(\s*)age = 35",
	      r"(\s*)gender = \"male\"",
	      r"(\s*)lucky_numbers = \[ 7, 11, 13, 17]"
    ]
    print("$$$$$$",[i for i, j in zip(original_input, content) if i == j ])


    # regex = r"print\('Your wedding will cost '\+str\(price\)\+' dollars'\);"
    # assert re.match(regex, content[(len(content)-1)])



@pytest.mark.it('STEP 3. Your code needs to print the correct sum on the console')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    print("@@@@", content)
    regex = r"print\(add_allFamilyLuckyNumbers\(Family\.members\)\) "
    assert re.match(regex, content[(len(content)-1)])
    # assert captured == str(94)+'\n'

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True