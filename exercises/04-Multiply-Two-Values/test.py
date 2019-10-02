import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re

@pytest.mark.it('1. You should create a variable named variables_are_cool')
def test_use_variable_name():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    regex = r"variables_are_cool(\s*)=(\s*)2345(\s*)\*(\s*)7323"
    # regex = r"color = \"red\""
    # regex = r"color(\s*)=(\s*)\"red\""
    assert re.match(regex, content[0])

@pytest.mark.it('2. You should print on the console the variables_are_cool value ')
def test_for_file_output(capsys):
    regex = r"print\(variables_are_cool\)"
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    # indices = [i for i, s in enumerate(content) if 'print' in s]
    # print(int(indices))
    my_print = [s for s in content if "print" in s]
    my_print_index = content.index(my_print[0])
    print(my_print_index)
    # print([s for s in content if "print" in s])
    my_result = 2345 *7323
    captured = buffer.getvalue()
    assert captured == str(my_result)+'\n'
    assert re.match(regex, content[my_print_index])
