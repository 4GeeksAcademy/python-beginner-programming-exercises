import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re

@pytest.mark.it('Function get_color should exist')
def test_for_file_output(capsys, app):
    try:
        app.get_color
    except AttributeError:
        raise AttributeError("The function 'get_color' should exist on app.py")
@pytest.mark.it('Function get_allStudentColors should exist')
def test_for_file_output(capsys, app):
    try:
        app.get_allStudentColors
    except AttributeError:
        raise AttributeError("The function 'get_allStudentColors' should exist on app.py")

@pytest.mark.it('Print the correct output on the console')
def test_for_file_output(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"print\(get_allStudentColors\(\)\)"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True

@pytest.mark.it('You should use for to iterate 10 times')
def test_for_file_output(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"for\s*"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True