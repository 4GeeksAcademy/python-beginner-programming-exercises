import io
import sys
sys.stdout = buffer = io.StringIO()
# from app import my_function
import pytest
import app
import os

path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Create a variable named 'color' with the string value 'red'")
def test_declare_variable():
    result = app.color
    assert  result == "red"

@pytest.mark.it("Create a variable named 'item' with the string value 'marker'")
def test_declare_variable():
    result = app.item
    assert  result == "marker"

@pytest.mark.it('The printed value on the console should be "red marker"')
def test_for_file_output(capsys):
    captured = buffer.getvalue()
    assert  "red marker\n" in captured 
