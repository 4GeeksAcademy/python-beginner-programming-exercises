import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re
import mock

@pytest.mark.it('The function get_allStudentColors should exist')
def test_function_existence():
    try:
        app.get_allStudentColors
    except AttributeError:
        raise AttributeError('The function get_allStudentColors should exist')

@pytest.mark.it('The function get_color should exist')
def test_function_existence():
    try:
        app.get_color
    except AttributeError:
        raise AttributeError('The function get_color should exist')

@pytest.mark.it('The function get_allStudentColors shuould call get_colors inside')
def test_function_inside_studentColors():
    with mock.patch('app.get_color') as mocked_get_color:
        from app import get_allStudentColors
        get_allStudentColors()
        mocked_get_color.assert_called_with(r"[red,yellow,blue,green]")

@pytest.mark.it('Print the function on the console')
def test_for_file_output(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"print\s*\(\*get_allStudentColors\(\)\s*\)"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True

