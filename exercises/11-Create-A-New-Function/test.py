import pytest
import app
import io
import os
import re
import sys
import mock
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function generate_random should exist')
def test_function_exists():
    try:
        from app import generate_random
    except ImportError:
        raise ImportError("The function 'generate_random' should exist on app.py")

@pytest.mark.it("The function 'generate_random' should return a random number between 0 and 9")
def test_for_return():
    from app import generate_random
    result = generate_random()
    assert result is not None
    for x in range(0,20):
        result = generate_random()
        assert result <= 9 and result >= 0 

@pytest.mark.it('Use the function randinit() or randrange()')
def test_for_type_random():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"random.randint\s*\(")
        regex2 = re.compile(r"random.randrange\s*\(")
        assert bool(regex.search(content)) == True or bool(regex2.search(content)) == True

@pytest.mark.it('You should print() the output of the function')
def test_function_called_for():
    
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(\s*generate_random\s*\(\s*\)\s*\)")
        assert bool(regex.search(content)) == True
