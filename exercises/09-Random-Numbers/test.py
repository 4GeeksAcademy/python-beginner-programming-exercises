import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import re

@pytest.mark.it("You should update only line 5 using randint()")
def test_conditional():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"random_number(\s*)=(\s*)random\.rand\w+\(1,10\)"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True

