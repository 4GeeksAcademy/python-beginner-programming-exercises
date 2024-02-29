import io
import sys
sys.stdout = buffer = io.StringIO()
from app import number_of_bottles
import pytest
import os
import app
import re

@pytest.mark.it('The function number_of_bottles must exist')
def test_function_spin_chamber(capsys, app):
    try:
        app.number_of_bottles
    except AttributeError:
        raise AttributeError("The function number_of_bottles should exist")

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    my_funcCall = [s for s in content if "def number_of_bottles():" in s]
    my_funcCallVar = content.index(my_funcCall[0])
    regex = r"def number_of_bottles\(\):"
    assert re.match(regex, content[my_funcCallVar])
    my_printCall = [s for s in content[3:] if "number_of_bottles()" in s]
    my_printCallVar = content.index(my_printCall[0])
    regex = r"number_of_bottles\(\)"
    assert re.match(regex, content[my_printCallVar])

@pytest.mark.it('The function must print the expected output')
def test_for_function_output(capsys):
    number_of_bottles()
    captured = capsys.readouterr()
    text=''
    for x in range(99,-1,-1):
        if (x==0):
            text+=("No more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall.\n")
        elif (x==1):
            text+=("1 bottle of milk on the wall, 1 bottle of milk.\nTake one down and pass it around, no more bottles of milk on the wall.\n")
        elif (x==2):
            text+=("2 bottles of milk on the wall, 2 bottles of milk.\nTake one down and pass it around, 1 bottle of milk on the wall.\n")
        else:
            text+=(str(x) + " bottles of milk on the wall, " + str(x) + " bottles of milk.\nTake one down and pass it around, " + str(x-1)+ " bottles of milk on the wall.\n")

    assert captured.out ==  text

