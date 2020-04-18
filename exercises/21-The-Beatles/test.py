import io
import sys
sys.stdout = buffer = io.StringIO()
from app import sing

import pytest
import os
import app
import re


@pytest.mark.it("1. You should declare a function named sing and call it in the correct way")
def test_functionSing():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_funcName = [s for s in content if "def sing():" in s]
    my_funcNameVar = content.index(my_funcName[0])
    regex = r"def sing\(\):"
    my_print = [s for s in content[2:] if "sing()" in s]
    my_printVar = content.index(my_print[0])
    regexPrint = r"sing\(\)"
    assert re.match(regex, content[my_funcNameVar])
    assert re.match(regexPrint, content[my_printVar])

@pytest.mark.it('2. Your function needs to print the correct output')
def test_for_function_output(capsys):
    sing()
    captured = capsys.readouterr()
    assert captured.out.lower() == "let it be,\nlet it be,\nlet it be,\nlet it be,\nwhisper words of wisdom, let it be, let it be,\nlet it be,\nlet it be,\nlet it be,\nthere will be an answer, let it be\n".lower()