import io
import sys
sys.stdout = buffer = io.StringIO()
from app import number_of_bottles
# from app import my_function
import pytest
import os
import app
import re



@pytest.mark.it('1. You need to declare a function called number_of_bottles that print the correct lyrics, and calling it correctly')
def test_for_file_output(capsys):

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

@pytest.mark.it('The function number_of_bottles should exist')
def test_function_existence(app):
    app.number_of_bottles

@pytest.mark.it('Your function needs to print the correct output')
def test_for_function_output(capsys):
    number_of_bottles()
    captured = capsys.readouterr()
    text1 = ""
    text2 = ""
    # first solution
    for x in reversed(range(100)):
        if (x==0):
            text1+="No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.\n"
        elif (x==1):
            text1+="1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.\n"
        elif (x==2):
            text1+="2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.\n"
        else:
            text1+=str(x)+" bottles of milk on the wall, "+str(x)+" bottles of milk. Take one down and pass it around, "+str(x-1)+" bottles of milk on the wall.\n"

    # second solution
    for x in range(99,1,-1): 
        if (x==2):
            text2+="2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall."
        else:
            text2+=str(x)+" bottles of milk on the wall, "+str(x)+" bottles of milk. Take one down and pass it around, "+str(x-1)+" bottles of milk on the wall."
    text2+="1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall."
    text2+="No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall."
        
    assert captured.out == text1 or captured.out == text2




# from unittest.mock import patch
# @pytest.mark.it('The function need to be printed in the console 100-99 times')
# @patch('builtins.print')
# def test_print_times(mock_print):
#     import app
#     from mock import call
#     app.number_of_bottles()
#     calls = []
#     calls2=[]
#     for x in reversed(range(100)):
#         if (x==0):
#             calls.append(call("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall."))
#         elif (x==1):
#             calls.append(call("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall."))
#         elif (x==2):
#             calls.append(call("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall."))
#         else:
#             calls.append(call(str(x)+" bottles of milk on the wall, "+str(x)+" bottles of milk. Take one down and pass it around, "+str(x-1)+" bottles of milk on the wall."))

#     for x in range(99,1,-1): 
#         if (x==2):
#             calls2.append(call("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall."))
#         elif (x>2):
#             calls2.append(call(str(x)+" bottles of milk on the wall, "+str(x)+" bottles of milk. Take one down and pass it around, "+str(x-1)+" bottles of milk on the wall."))
#     calls2.append(call("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall."))
#     calls2.append(call("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall."))
    
#     mock_print.assert_has_calls(calls, any_order=False) or mock_print.assert_has_calls(calls2, any_order=False)