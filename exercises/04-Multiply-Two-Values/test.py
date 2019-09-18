import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app

@pytest.mark.it('1. You should create a variable named variables_are_cool')
def test_use_variable_name():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("variables_are_cool") > 0

@pytest.mark.it('2. You should print on the console the variables_are_cool value ')
def test_for_file_output(capsys):
    my_result = 2345 *7323
    captured = buffer.getvalue()
    assert captured == str(my_result)+'\n'
