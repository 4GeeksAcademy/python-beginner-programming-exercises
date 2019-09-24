import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
# @pytest.mark.it('Your code needs to print hello on the console')
# def test_for_file_output(capsys):
#     captured = buffer.getvalue()
#     assert captured == "hello\n" #add \n because the console jumps the line on every print
@pytest.mark.it('Print "Hello, --Your Name--"')
def test_desired_output(capsys):
    app.is_odd(32345)
    captured = capsys.readouterr()

    assert captured.out == "true\n"
@pytest.mark.it("Using the conditional statement")
def test_conditional():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    print("test:",content)
    assert content.find("my_number") > 0

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True