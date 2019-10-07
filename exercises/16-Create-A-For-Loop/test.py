import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re

@pytest.mark.it("1. You should declare a function named standards_maker")
def test_function_name():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "def standards_maker():" in s]
    my_printVar = content.index(my_print[0])
    regex = r"def standards_maker\(\):"
    assert re.match(regex, content[my_printVar])

@pytest.mark.it("2. You should include in the function standards_maker a for loop which prints the string in the instructions 300 times")
def test_print():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_for = [s for s in content if "for x in range(300):" in s]
    my_forVar = content.index(my_for[0])
    regex_for = r"for x in range\(300\):"
    my_print = [s for s in content if 'print("I will write questions if I am stuck")' in s]
    my_printVar = content.index(my_print[0])
    regex_print = r"print\(\"I will write questions if I am stuck\"\)"

    assert re.match(regex_for, content[my_forVar])
    assert re.match(regex_print, content[my_printVar])

@pytest.mark.it("3. You should call the function standards_maker ")
def test_callTheFunction():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_call = [s for s in content[2:] if "standards_maker()" in s]
    my_callVar = content.index(my_call[0])
    print("###",my_callVar)
    regex_call = r"standards_maker\(\)"


    assert re.match(regex_call, content[my_callVar])
