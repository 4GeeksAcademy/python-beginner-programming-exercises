import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re

@pytest.mark.it('1. You should create a function called generate_random ')
def test_for_function(capsys):
    regex = r"def generate_random\(\):"
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    # indices = [i for i, s in enumerate(content) if 'print' in s]
    # print(int(indices))
    my_func = [s for s in content if "def generate" in s]
    my_func_index = content.index(my_func[0])
    print(my_func_index)
    # print([s for s in content if "print" in s])
    assert re.match(regex, content[my_func_index])

@pytest.mark.it("2. The function should generate and print a random number between 0 and 9")
def test_print():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "print" in s]
    my_printVar = content.index(my_print[0])
    regex = r"print\(random\.rand\w+\(\d+\D*\d+\)\)"
    assert re.match(regex, content[my_printVar])
@pytest.mark.it('3. You should call your function in the correct way ')
def test_for_file_output(capsys):
    regex = r"generate_random\(\)"
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    # indices = [i for i, s in enumerate(content) if 'print' in s]
    # print(int(indices))
    my_func = [s for s in content if "generate_random()" in s]
    my_func_index = content.index(my_func[0])
    print(my_func_index)
    # print([s for s in content if "print" in s])
    assert re.match(regex, content[(len(content)-1)])

# @pytest.mark.it('Your code needs to print hello on the console')
# def test_generate_random(capsys):
#     x = get_generate_random()
#     print("x", x)
#     captured = buffer.getvalue()
#     assert captured == "hello\n" #add \n because the console jumps the line on every print

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True