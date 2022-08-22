import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import re
import app


@pytest.mark.it("You should be printing the get_randomInt function")
def test_only_change_line_5():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        line = r"print\s*\(\s*get_randomInt\s*\(\s*\)\s*\)"
        regex = re.compile(line)
        assert bool(regex.search(content)) == True

@pytest.mark.it("get_randomInt function should exist")
def test_function_exists():
    try:
        assert app.get_randomInt()
    except AttributeError:
        raise AttributeError('The function "get_randomInt" should exist')

@pytest.mark.it("get_randomInt function should return a random integer between 1 and 10")
def test_function_returns_random_integer():
    try:
        for i in range(10):
            # only asserting if value is outside the range, else it will pass
            result = app.get_randomInt()
            assert result >= 1 and result <= 10
    except AttributeError:
        raise AttributeError('The function "get_randomInt" is returning values outside the specified range')

@pytest.mark.it("get_randomInt function should NOT be returning a static integer value")
# in case user returns single value between [1 and 10]
def test_function_return_no_static():
    try:
        tries = 0
        output = app.get_randomInt()
        for i in range(10):
            if output == app.get_randomInt():
                tries+=1
                # only asserting if value is outside the range, else it will pass
        assert tries < 10
    except AttributeError:
        raise AttributeError('The function "get_randomInt" is returning a static value, not a random one')
