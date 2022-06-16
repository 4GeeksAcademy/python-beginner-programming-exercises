import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function get_randomInt should exist')
def test_function_existence(app):
    try:
        app.get_randomInt
    except AttributeError:
        raise AttributeError("The function get_randomInt should exist")


@pytest.mark.it("Check that you are setting the correct values for the randrange function.")
def test_conditional():
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"random\.randrange+\(1, 13\)"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True

@pytest.mark.it('The console must return numbers between 1 and 12 included')
def test_print_output(capsys, app):
    result = app.get_randomInt()
    assert result >= 1 or result <= 12


@pytest.mark.it('You must call the function inside the print() function.')
def test_function_called_for():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(\s*get_randomInt\(\)\s*\)")
        assert bool(regex.search(content)) == True