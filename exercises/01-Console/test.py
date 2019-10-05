import io
import sys
sys.stdout = buffer = io.StringIO()
import app
import re
import os
import pytest

@pytest.mark.it('1. Your code needs to print Hello World! on the console')
def test_for_file_output(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "print" in s]
    my_printIndex = content.index(my_print[0])
    # print(my_print_index)
    regex = r"print\(\"Hello World!\"\)"
    assert re.match(regex, content[my_printIndex])
    captured = buffer.getvalue()
    assert captured == "Hello World!\n" #add \n because the console jumps the line on every print

