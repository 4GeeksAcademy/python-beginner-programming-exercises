import io
import sys
sys.stdout = buffer = io.StringIO()

import pytest
import os
import app
import re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function start_counting should exist')
def test_function_existence():
    assert hasattr(app, 'start_counting')

@pytest.mark.it('The function start_counting should return the expected output')
def test_function_output(capsys):
    app.start_counting()
    captured = capsys.readouterr()
    assert "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n" in captured.out

@pytest.mark.it('Use a for loop')
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        assert "for" in content
