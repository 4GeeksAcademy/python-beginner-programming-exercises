import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re
@pytest.mark.it("1. You should declare a function named standards_maker")
def test_while_loop():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_while = [s for s in content if "while counter > -1:" in s]
    my_whileVar = content.index(my_while[0])
    regex = r"while counter(\s*)>(\s*)-1:"
    assert re.match(regex, content[my_whileVar])

# @pytest.mark.it('2. The console should print numbers from 100 to 1')
# def test_for_file_output(capsys):
#     def test():
#         counter = 100
#         while counter > 0:
#             print(counter)
#             counter-=1
#         return counter
#     captured = buffer.getvalue()
#     assert captured == str(test())+'\n'