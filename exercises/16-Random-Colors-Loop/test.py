import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re

@pytest.mark.it('Print the correct output on the console')
def test_for_file_output(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"print\(get_allStudentColors\(\)\)"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True