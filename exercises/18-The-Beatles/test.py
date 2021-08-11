import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
from app import sing
import pytest
import app
import re
import os

@pytest.mark.it("You should declare a function named sing and call it in the correct way")
def test_function_sing_exists(app):
    try:
        app.sing
    except AttributeError:
        raise AttributeError("The function 'sing' should exist on app.py")

@pytest.mark.it('Your function needs to print the correct output')
def test_for_function_output(capsys):
    sing()
    captured = capsys.readouterr()
    assert captured.out.lower() == "let it be,\nlet it be,\nlet it be,\nlet it be,\nwhisper words of wisdom, let it be, let it be,\nlet it be,\nlet it be,\nlet it be,\nthere will be an answer, let it be\n".lower()