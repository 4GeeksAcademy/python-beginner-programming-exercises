import io
import sys
sys.stdout = buffer = io.StringIO()
import app
# from app import my_function
import pytest

@pytest.mark.it('Your code needs to print Yellow on the console')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert captured == "Yellow\n" #add \n because the console jumps the line on every print

