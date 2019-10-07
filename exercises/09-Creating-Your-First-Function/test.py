import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re


@pytest.mark.it("1. You should add the return statement inside the existing function")
def test_use_my_var1():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_return = [s for s in content if "return" in s]
    my_returnIndex = content.index(my_return[0])
    # print(my_print_index)
    regex = r"return a(\s*)\+(\s*)b"
    assert re.match(regex, content[my_returnIndex])

#     assert re.match(regex, content)
@pytest.mark.it('2. The console should return 7')
def test_add_variables(capsys):
    captured = buffer.getvalue()
    assert captured == str(7)+"\n"
