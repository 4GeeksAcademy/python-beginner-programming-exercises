import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import re
import os


@pytest.mark.it('1. Your code needs to print the correct output on the console')
def test_for_file_output(capsys):

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_codeCall = [s for s in content[3:] if "print(fire_gun())" in s]
    my_codeCallVar = content.index(my_codeCall[0])
    regex = r"print\(fire_gun\(\)\)"
    assert re.match(regex, content[my_codeCallVar])

