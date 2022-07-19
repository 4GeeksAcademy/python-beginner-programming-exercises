import io
import sys
sys.stdout = buffer = io.StringIO()
# from app import my_function
import pytest
import os
import app
import re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('You should create a variable named variables_are_cool')
def test_variable_exists():
    try:
        from app import variables_are_cool
    except ImportError:
        raise ImportError("The variable 'variables_are_cool' should exist on app.py")

@pytest.mark.it('Variables_are_cool value should be like 2345 * 7323 ')
def test_use_variable_name():
    result = app.variables_are_cool == 17172435
    assert result == True

@pytest.mark.it('Print on the console the variables_are_cool value ')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert captured == '17172435\n'