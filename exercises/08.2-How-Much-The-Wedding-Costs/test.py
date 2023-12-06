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
        regex2 = re.compile(r"elif\s*")
        assert bool(regex2.search(content)) == True


@pytest.mark.it("Between 101 and 200 guests sould be priced 15,000")
def test__between_100_and_200(capsys, app):
    with mock.patch('builtins.input', lambda x: 200):
        app()
        captured = capsys.readouterr()
        price = 15000
        assert "Your wedding will cost "+str(price)+" dollars\n" in captured.out


@pytest.mark.it("Between 51 and 100 guests sould be priced 10,000")
def test_between_101_and_51(capsys, app):
    with mock.patch('builtins.input', lambda x: 100):
        app()
        captured = capsys.readouterr()
        price = 10000
        assert "Your wedding will cost "+str(price)+" dollars\n" in captured.out


@pytest.mark.it("Less than 50 guests, it should cost 4,000")
def test_less_than_50(capsys, app):
    with mock.patch('builtins.input', lambda x: 50):
        app()
        captured = capsys.readouterr()
        price = 4000
        "Your wedding will cost "+str(price)+" dollars\n" in captured.out

@pytest.mark.it("More than 200 guests, it should cost 20,000")
def test_t(capsys, app):
    with mock.patch('builtins.input', lambda x: 201):
        app()
        captured = capsys.readouterr()
        price = 20000
        "Your wedding will cost "+str(price)+" dollars\n" in captured.out
