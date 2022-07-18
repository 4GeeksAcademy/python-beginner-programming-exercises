import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import re

@pytest.mark.it("You should edit the function randint() to generate a random number between 1 and 10")
def test_conditional():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"random_number(\s*)=(\s*)random\.rand\w+(\s)*\((\s)*1(\s)*,(\s)*10(\s)*\)"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True

@pytest.mark.it("You should only change line 5")
def test_only_change_line_5():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        line_1 = r"import(\s)random"
        line_2 = r"def(\s)get_randomInt\((\s*)\)(\s*)\:"
        line_3 = r"return(\s)random_number"
        line_4 = r"print(\s*)\(get_randomInt(\s*)\((\s*)\)(\s*)\)"

        regex_1 = re.compile(line_1)
        regex_2 = re.compile(line_2)
        regex_3 = re.compile(line_3)
        regex_4 = re.compile(line_4)

        assert bool(regex_1.search(content)) == True
        assert bool(regex_2.search(content)) == True
        assert bool(regex_3.search(content)) == True
        assert bool(regex_4.search(content)) == True