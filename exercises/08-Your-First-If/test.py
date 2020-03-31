# from app import my_function
import pytest,os,re,io,sys, mock, json

@pytest.mark.it('Use the function print()')
def test_for_print(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\(.+\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("When input for more than 100 it should print: Give me your money!")
def test_for_more(stdin, capsys, app):
    with mock.patch('builtins.input', lambda x: 101):
        app()
        captured = capsys.readouterr()
        assert "Give me your money!\n" == captured.out

@pytest.mark.it("When input exactly 100 should print: Buy me some coffee you cheap ")
def test_between(capsys, app):
    with mock.patch('builtins.input', lambda x: 100):
        app()
        captured = capsys.readouterr()
        assert "Buy me some coffee you cheap!\n" == captured.out

@pytest.mark.it("When input exactly 50 should print: You are a poor guy, go away")
def test_for_less(capsys, app):
    with mock.patch('builtins.input', lambda x: 50):
        app()
        captured = capsys.readouterr()
        assert "You are a poor guy, go away!\n" == captured.out




