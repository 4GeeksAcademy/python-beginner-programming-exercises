import io
import sys
sys.stdout = buffer = io.StringIO()
import app
# from app import my_function
import pytest
import os
import re

# @pytest.mark.it('1. Declare a variable with a string value "Yellow" ')
# def test_for_regex(capsys):
#     f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
#     content = f.readlines()
#     content = [x.strip() for x in content]

#     # variable = 'name = "Yellow"'
#     variable = r"\w(\s*)=(\s*)\"Yellow\""
#     assert re.match(variable, content[0])

@pytest.mark.it('1. Your code needs to print Yellow on the console')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert captured == "Yellow\n" #add \n because the console jumps the line on every print

