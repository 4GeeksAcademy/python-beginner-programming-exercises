import io
import sys
sys.stdout = buffer = io.StringIO()
from app import fizz_buzz
# from app import my_function
import pytest
import app
import os
import re

@pytest.mark.it("1. Don't change or remove the existing code")
def test_forExistingCode(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_code = [s for s in content if "def fizz_buzz():" in s]
    my_codeVar = content.index(my_code[0])
    regex = r"def fizz_buzz\(\):"
    my_codeCall = [s for s in content[3:] if "fizz_buzz()" in s]
    my_codeCallVar = content.index(my_codeCall[0])
    regexCall = r"fizz_buzz\(\)"

    assert re.match(regex, content[my_codeVar])
    assert re.match(regexCall, content[my_codeCallVar])
    
@pytest.mark.it('2. Your function needs to print the correct output')
def test_for_function_output(capsys):
    fizz_buzz()
    captured = capsys.readouterr()
    assert captured.out == "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n"
