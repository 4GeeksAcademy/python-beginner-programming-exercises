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
    assert app.number_of_bottles

@pytest.mark.it('The function must return the expected output')
def test_for_function_output(capsys):
    number_of_bottles()
    captured = capsys.readouterr()
    text=''
    for x in range(99,-1,-1):
        if (x==0):
            text+=("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.\n")
        elif (x==1):
            text+=("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.\n")
        elif (x==2):
            text+=("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.\n")
        else:
            text+=(str(x) + " bottles of milk on the wall, " + str(x) + " bottles of milk. Take one down and pass it around, " + str(x-1)+ " bottles of milk on the wall.\n")
    assert captured.out == text

