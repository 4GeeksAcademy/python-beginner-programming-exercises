# from app import my_function
import pytest,os,re,io,sys, mock, json
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('Use the if statement')
def test_for_print(capsys):
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if\s*")
        assert bool(regex.search(content)) == True

@pytest.mark.it('Use the elif statement')
def test_for_print(capsys):
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if\s*")
        regex2 = re.compile(r"elif\s*")
        assert ((bool(regex.search(content)) == True) and (bool(regex2.search(content))==True))

@pytest.mark.it('Use the function print()')
def test_for_print(capsys):
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it("When input for more than 100 it should print: Give me your money!")
def test_for_output_when_101(stdin, capsys, app):
    with mock.patch('builtins.input', lambda x: 101):
        app()
        captured = capsys.readouterr()
        assert "Give me your money!\n" in captured.out 

@pytest.mark.it("When input exactly 100 should print: Buy me some coffee you cheap ")
def test_for_output_when_100(capsys, app):
    with mock.patch('builtins.input', lambda x: 100):
        app()
        captured = capsys.readouterr()
        assert "Buy me some coffee you cheap!\n" in captured.out

@pytest.mark.it("When input is 99 should print: Buy me some coffee you cheap ")
def test_for_output_when_99(capsys, app):
    with mock.patch('builtins.input', lambda x: 99):
        app()
        captured = capsys.readouterr()
        assert "Buy me some coffee you cheap!\n" in captured.out

@pytest.mark.it("When input is 51 should print: Buy me some coffee you cheap ")
def test_for_output_when_51(capsys, app):
    with mock.patch('builtins.input', lambda x: 51):
        app()
        captured = capsys.readouterr()
        assert "Buy me some coffee you cheap!\n" in captured.out

@pytest.mark.it("When input exactly 50 should print: You are a poor guy, go away")
def test_for_output_when_50(capsys, app):
    with mock.patch('builtins.input', lambda x: 50):
        app()
        captured = capsys.readouterr()
        assert "You are a poor guy, go away!\n" in captured.out

@pytest.mark.it("When input less than 50 should print: You are a poor guy, go away")
def test_for_output_when_49(capsys, app):
    with mock.patch('builtins.input', lambda x: 49):
        app()
        captured = capsys.readouterr()
        assert "You are a poor guy, go away!\n" in captured.out