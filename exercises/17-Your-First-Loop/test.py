import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re


@pytest.mark.it("1. You should fix the existing code")
def test_existingCode():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    # content = [x.strip() for x in content]  ####  With this line of code I removed all the whitespace characters like `\n` at the end of each line
    # print("$$$$", content)
    price_variable = (r"def start_counting\(\):	\n"
	      r"(\s*)for i in range\(101\):\n"
	      r"(\s*)print\(i\)	\n"
	      r"(\s+)return i\n\n"
	      r"start_counting\(\)")
    assert re.match(price_variable, content)

# @pytest.mark.it('The console should count from 0 to 100')
# def test_for_file_output(capsys):
#     def start_counting():
# 	      for i in range(101):
# 		        print(i)

#     captured = buffer.getvalue()
#     print("test",start_counting())
#     assert captured == str(start_counting())+'\n'

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True