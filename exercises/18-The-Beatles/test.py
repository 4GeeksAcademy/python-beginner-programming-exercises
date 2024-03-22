import os
import re
import app
import pytest
import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function


@pytest.mark.it("You should declare a function named sing()")
def test_function_sing_exist(app):
    try:
        assert app.sing
    except AttributeError:
        raise AttributeError("The function 'sing' should exist on app.py")


@pytest.mark.it("You should not be hard coding the output")
def test_function_hardcode_output():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\breturn\s*[^\"][a-zA-Z0-9]*\b\s*")
        assert bool(regex.search(content)) == True


@pytest.mark.it("The function sing() should return a string with the song lyrics")
def test_function_sing_return(app):
    try:
        assert app.sing() == "let it be,\nlet it be,\nlet it be,\nlet it be,\nthere will be an answer,\nlet it be,\nlet it be,\nlet it be,\nlet it be,\nlet it be,\nwhisper words of wisdom, let it be"
    except AttributeError:
        raise AttributeError("The function 'sing' should exist on app.py")
