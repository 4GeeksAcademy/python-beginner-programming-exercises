import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re

@pytest.mark.it('You should create a variable named variables_are_cool')
def test_variable_exists():
    try:
        from app import variables_are_cool
    except ImportError:
        raise ImportError("The variable 'variables_are_cool' should exist on app.py")

@pytest.mark.it('Variables_are_cool value should be like 2345 * 7323 ')
def test_use_variable_name():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"variables_are_cool(\s*)=(\s*)2345(\s*)\*(\s*)7323")
        assert bool(regex.search(content)) == True

@pytest.mark.it('Print on the console the variables_are_cool value ')
def test_for_file_output(capsys):

    from app import variables_are_cool
    captured = buffer.getvalue()
    assert captured == str(variables_are_cool)+'\n'