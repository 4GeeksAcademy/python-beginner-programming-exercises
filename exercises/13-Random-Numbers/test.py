import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import re

@pytest.mark.it("You should update only line 5 using randint()")
def test_conditional():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "random_number =" in s]
    my_printVar = content.index(my_print[0])
    regex = r"random_number(\s*)=(\s*)random\.rand\w+\(1,10\)"
    assert re.match(regex, content[my_printVar])

