import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re

@pytest.mark.it("You should declare a function named standards_maker")
def test_variable_exists():
    try:
        from app import standards_maker
    except ImportError:
        raise ImportError("The function 'standards_maker' should exist on app.py")

@pytest.mark.it("You should include in the function standards_maker a for loop which prints the string in the instructions 300 times")
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    expected = ["I will write questions if I am stuck\n" for x in range(300)]
    assert captured == "".join(expected) #add \n because the console jumps the line on every print

@pytest.mark.it('Use the function print()')
def test_for_print():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\(.+\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You should call the function standards_maker ")
def test_callTheFunction():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"standards_maker\(\)"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True
