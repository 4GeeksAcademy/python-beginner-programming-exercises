import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re


@pytest.mark.it("1. You should return a list of number between 0 and 100")
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert captured == "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n" #add \n because the console jumps the line on every print
