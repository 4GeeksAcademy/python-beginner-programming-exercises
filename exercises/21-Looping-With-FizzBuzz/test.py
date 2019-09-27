import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re

@pytest.mark.it('STEP 3. Your code needs to print the correct output on the console')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    print("@@@@", content)
    regex = r"fizz_buzz\(\)"
    assert re.match(regex, content[(len(content)-1)])

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True