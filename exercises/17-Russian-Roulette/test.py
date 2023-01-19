import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import re
import os

@pytest.mark.it('The function spin_chamber must exist')
def test_function_spin_chamber(capsys, app):
    assert app.spin_chamber

@pytest.mark.it('The function fire_gun must exist')
def test_function_fire_gun(capsys, app):
    assert app.fire_gun

@pytest.mark.it('The function fire_gun should return the expected output in both cases')
def test_function_output(capsys, app):
    if(app.spin_chamber() == app.bullet_position):
        assert app.fire_gun() == "You are dead!"
    else:
        assert app.fire_gun() == "Keep playing!"

@pytest.mark.it('Your code needs to print the correct output on the console')
def test_for_file_output(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_codeCall = [s for s in content[3:] if "print(fire_gun())" in s]
    my_codeCallVar = content.index(my_codeCall[0])
    regex = r"print\(fire_gun\(\)\)"
    assert re.match(regex, content[my_codeCallVar])



