import io
import sys
sys.stdout = buffer = io.StringIO()
import app
import re
import os
import pytest

@pytest.mark.it('Use the function print()')
def test_for_file_output(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"print\s*\("
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True

@pytest.mark.it('Print Hello World! on the console')
def test_for_console_log(capsys):
    captured = buffer.getvalue()
    assert captured == "Hello World!\n" #add \n because the console jumps the line on every print

