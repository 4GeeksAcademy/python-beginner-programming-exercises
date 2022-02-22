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

# @pytest.mark.it('Print the correct output on the console')
# def test_for_file_output(capsys):
#     path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
#     with open(path, 'r') as content_file:
#         content = content_file.read()
#         pattern = r"print\(get_allStudentColors\(\)\)"
#         regex = re.compile(pattern)
#         assert bool(regex.search(content)) == True


from unittest.mock import patch
@pytest.mark.it('You should use print 10 times')
@patch('builtins.print')
def test_print_times(mock_print):
    # The actual test
    # import the function that use print 
    from app import get_allStudentColors
    get_allStudentColors()

    # we need the call format to know how many calls print has.
    from mock import call
    calls = []
    for x in range(10):
        calls.append(call(x))
    # calls = [call(0),call(1),call(2),call(3),call(4),call(5),call(6),call(7),call(8),call(9)]
    mock_print.assert_has_calls(calls, any_order=False) # set any_order to False to respect the iteration sequence (0,1,2,3,4...etc.)


@pytest.mark.it('You should use for to iterate 10 times')
def test_for_file_output(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"for\s*"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True