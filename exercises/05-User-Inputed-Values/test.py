import io
import sys
sys.stdout = buffer = io.StringIO()
sys.stdin = buffer = input()
# from app import my_function
import pytest
import app
import os

# @pytest.mark.it('1. You should print on the console the input value + 10')
# def test_use_variable_name():

#     f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
#     content = f.read()
#     assert content.find("console") > 0
@pytest.mark.it('3. Your code needs to print Hello World on the console')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    inp = buffer.getvalue() +10
    assert captured == inp+"\n" #add \n because the console jumps the line on every print
# @pytest.mark.it('2. You should print on the console the variables_are_cool value ')
# def test_for_file_output(capsys):
#     my_result = 2345 *7323
#     captured = stdin
#     assert captured == str(my_result)+'\n'