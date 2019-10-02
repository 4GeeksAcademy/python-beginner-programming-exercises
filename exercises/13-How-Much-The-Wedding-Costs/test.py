import io
import sys

# from app import my_function
import pytest
import app
import os
import re


@pytest.mark.it("1. You should not delete or change the existing code")
def test_existing_code():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()

    original_input = r"# user_input = int\(input\('How many people are coming to your wedding\?'\)\)"
    assert re.match(original_input, content[0])
    regex = r"print\('Your wedding will cost '\+str\(price\)\+' dollars'\);"
    assert re.match(regex, content[(len(content)-1)])

@pytest.mark.it("2. You should create a price variable before the if statement")
def test_existingPriceVariable():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]  ####  With this line of code I removed all the whitespace characters like `\n` at the end of each line
    price_variable = r"price = (.+)"
    assert re.match(price_variable, content[2])
    # for price in content:
    #     if price == price_variable:
    #         assert re.match(price_variable, price)
    # for price in content:
    #     price_index = content.index(price)
    #     if re.match(price_variable, price_index):
    #         if price_index < 3:



@pytest.mark.it('3. Your code needs to print the correct outpu on the console')
def test_for_file_output():
    # sys.stdout = buffer = io.StringIO()
    test =sys.stdin.read()
    # captured = buffer.getvalue()
    # print("####",buffer.getvalue())
    print("$$$$",test)
    # assert captured == "hello\n" #add \n because the console jumps the line on every print

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True