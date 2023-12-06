import pytest
import app
import os
import io
import re
import mock
import sys
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function add_numbers should exist')
def test_for_function():
    try:
        app.add_numbers
    except AttributeError:
        raise AttributeError("The function add_numbers should exist")

@pytest.mark.it('Print the function in console with the values: 3, 4')
def test_for_function_print():
    
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(\s*add_numbers\s*\(\s*3\s*,\s*4\s*\)\s*\)")
        assert bool(regex.search(content)) == True


@pytest.mark.it('Use the function print()')
def test_for_print():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('Function should sum the two given numbers')
def test_for_return():
    from app import add_numbers
    result = add_numbers(3,4)
    assert result == 7

@pytest.mark.it('Function should sum the two given numbers. Testing with different numbers')
def test_for_return_2():
    from app import add_numbers
    result = add_numbers(10,5)
    assert result == 15
