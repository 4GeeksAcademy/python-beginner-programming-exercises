import io
import sys
sys.stdout = buffer = io.StringIO()
import app

import pytest

@pytest.mark.it('1. Your code needs to print Hello World! on the console')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert captured == "Hello World!\n" #add \n because the console jumps the line on every print

