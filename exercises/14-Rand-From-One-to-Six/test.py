import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re

@pytest.mark.it("You should return a random number between 1 and 12 included")
def test_conditional():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"random_number(\s*)=(\s*)random\.randrange+\(1,13\)"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True