import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re

@pytest.mark.it('Function get_color should exist')
def test_get_color_exists(capsys, app):
    try:
        app.get_color
    except AttributeError:
        raise AttributeError("The function 'get_color' should exist on app.py")
@pytest.mark.it('Function get_allStudentColors should exist')
def test_get_allStudentColors_exists(capsys, app):
    try:
        app.get_allStudentColors
    except AttributeError:
        raise AttributeError("The function 'get_allStudentColors' should exist on app.py")

@pytest.mark.it('Function get_allStudentColors should return ten colors')
def test_ten_colors(capsys, app):
    result = app.get_allStudentColors()
    assert len(result) == 10

@pytest.mark.it("Function get_allStudentColors shouldn't return an array with the black color")
def test_black_in_array(capsys, app):
    result = app.get_allStudentColors()
    assert result.count("black") == 0

@pytest.mark.it('You should use a for loop to iterate 10 times')
def use_for_loop(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"for\s*"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True
