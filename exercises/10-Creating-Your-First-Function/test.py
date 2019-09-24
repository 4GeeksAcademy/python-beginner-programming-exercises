import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re

# @pytest.mark.it('1. You should return the result of a + b ')
# def test_add_number():
#     regex = (r"def add_numbers\(a,b\):\n"
# 	    r"  	return a\s*\+\s*b")
#     # regex = (r"def add_numbers\(a,b\):\n"
# 	  #   r"  	return a\s*\+\s*b")
#     f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
#     content = f.read()
#     print("content", content)
#     # matches = re.finditer(regex, content, re.MULTILINE)
#     print("matches",regex)


#     assert re.match(regex, content)
@pytest.mark.it('Add all three numbers')
def test_add_variables(capsys):
    app.add_numbers(3,4)
    captured = capsys.readouterr()
    print(captured.out)

    if captured.out == str(7) + "\n":
        assert True
    else:
        assert False
# @pytest.mark.it('2. Your code needs to print 7 on the console')
# def test_for_file_output(capsys):
#     my_result = 3+4
#     captured = buffer.getvalue()
#     assert captured == str(my_result)+"\n" #add \n because the console jumps the line on every print
# @pytest.mark.it('2. You should print on the console the variables_are_cool value ')
# def test_for_file_output(capsys):
#     my_result = 2345 *7323
#     captured = buffer.getvalue()
#     assert captured == str(my_result)+'\n'
# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True