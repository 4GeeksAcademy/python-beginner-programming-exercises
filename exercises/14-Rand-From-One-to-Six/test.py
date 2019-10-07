import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re

@pytest.mark.it("1. You should return a random number between 1 and 12 included")
def test_conditional():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "random_number =" in s]
    my_printVar = content.index(my_print[0])
    regex = r"random_number(\s*)=(\s*)random\.randrange+\(13\)"
    assert re.match(regex, content[my_printVar])
