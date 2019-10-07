import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re




@pytest.mark.it('1. You should change the fourth lucky number of John Doe!')
def test_forLuckyNumber(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "Person.lucky_numbers" in s]
    my_printVar = content.index(my_print[0])
    regex = r"Person\.lucky_numbers\[3](\s*)=(\s*)33"
    assert re.match(regex, content[my_printVar])
@pytest.mark.it('2. You should create a new person and then add it to the familoy object')
def test_forFamilyMember(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "Family.members.append" in s]
    my_printVar = content.index(my_print[0])
    regex = r"Family\.members\.append\(\w+\)"
    assert re.match(regex, content[my_printVar])

@pytest.mark.it('3. Your code needs to print the SUM of all the lucky numbers of the Doe family on the console')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "print(add_allFamilyLuckyNumbers(Family.members))" in s]
    my_printVar = content.index(my_print[0])
    regex = r"print\(add_allFamilyLuckyNumbers\(Family\.members\)\)"
    assert re.match(regex, content[my_printVar])
    assert captured == str(94)+"\n"


    # assert captured == str(94)+'\n'

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True