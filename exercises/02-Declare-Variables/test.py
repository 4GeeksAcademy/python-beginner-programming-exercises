import io
import sys
sys.stdout = buffer = io.StringIO()
import app
# from app import my_function
import pytest
import os
import re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('Use the function print()')
def test_for_print():
    
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(['\"]?.+['\"]?\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it('Declare a variable and assign it the value "Yellow"')
def test_for_variable():
    
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\w*(\s*)=(\s*)(\"|\')Yellow(\"|\')")
        assert bool(regex.search(content)) == True

@pytest.mark.it('Print the variable on the console')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert   "Yellow\n" in captured #add \n because the console jumps the line on every print

    
