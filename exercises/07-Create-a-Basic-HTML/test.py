import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re


@pytest.mark.it('1. Your code needs to print a basic html layout on the console')
def test_for_file_output(capsys):
    regex = r"print(\s*)\(html_document\)"
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    # indices = [i for i, s in enumerate(content) if 'print' in s]
    # print(int(indices))
    my_print = [s for s in content if "print" in s]
    my_print_index = content.index(my_print[0])
    captured = buffer.getvalue()
    assert re.match(regex, content[my_print_index])
    assert captured == "<html><head><title></title></head><body></body></html>\n" #add \n because the console jumps the line on every print
@pytest.mark.it("2. You should create a variable named html_document")
def test_use_my_var1():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "html_document =" in s]
    my_htmlDocumentIndex = content.index(my_print[0])
    # print(my_print_index)
    regex = r"html_document(\s*)=(\s*)e(\s*)\+(\s*)c(\s*)\+(\s*)g(\s*)\+(\s*)a(\s*)\+(\s*)f(\s*)\+(\s*)h(\s*)\+(\s*)d(\s*)\+(\s*) b"
    assert re.match(regex, content[my_htmlDocumentIndex])
