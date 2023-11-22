import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import re
import os

@pytest.mark.it("You should declare a function named sing()")
def test_function_sing_exists(app):
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
def test_function_sing_exists(app):
    try:
        assert app.sing() == "let it be, let it be, let it be, let it be, there will be an answer, let it be, let it be, let it be, let it be, let it be, whisper words of wisdom, let it be"
    except AttributeError:
        raise AttributeError("The function 'sing' should exist on app.py")
