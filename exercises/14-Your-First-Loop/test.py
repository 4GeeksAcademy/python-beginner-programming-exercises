import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function start_counting should exist')
def test_for_function_existence():
    try:
        app.start_counting
    except AttributeError:
        raise AttributeError('The function start_counting should exist')

@pytest.mark.it('The function start_counting should return the expected output')
def test_for_function_output(capsys):
    app.start_counting()
    captured = capsys.readouterr()
    assert "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n" == captured.out

@pytest.mark.it('Use for loop')
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for\s*")
        assert bool(regex.search(content)) == True