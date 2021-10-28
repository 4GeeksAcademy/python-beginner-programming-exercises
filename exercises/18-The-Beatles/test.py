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
        assert app.sing
    except AttributeError:
        raise AttributeError("The function 'sing' should exist on app.py")

@pytest.mark.it("The function sing, should print the correct string in the console")
def test_for_file_output(capsys, app):
    app.sing()
    captured = capsys.readouterr()
    assert captured.out == "let it be, let it be, let it be, let it be, whisper words of wisdom, let it be, let it be, let it be, let it be, let it be, there will be an answer, let it be\n"