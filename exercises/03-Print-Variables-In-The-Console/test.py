import io
import sys
sys.stdout = buffer = io.StringIO()
# from app import my_function
import pytest
import app
import os
import re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Create a variable named 'color' with the string value red")
def test_declare_variable():
    result = app.color
    assert result == "red"

@pytest.mark.it('Print on the console the value of the variable ')
def test_for_printing_variable():
   
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(\s*color\s*\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The printed value on the console should be "red"')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert captured == "red\n"