# from app import my_function
import pytest,os,re,io,sys, mock, json

@pytest.mark.it("Between 101 and 199 guests sould be priced 15,000")
def test__between_100_and_200(capsys, app):
    with mock.patch('builtins.input', lambda x: 199):
        app()
        captured = capsys.readouterr()
        price = 15000
        assert "Your wedding will cost "+str(price)+" dollars\n" == captured.out

@pytest.mark.it("Between 100 and 51 guests sould be priced 10,000")
def test_between_101_and_51(capsys, app):
    with mock.patch('builtins.input', lambda x: 100):
        app()
        captured = capsys.readouterr()
        price = 10000
        assert "Your wedding will cost "+str(price)+" dollars\n" == captured.out


@pytest.mark.it("Less than 50 guests sould be priced 4,000")
def test_less_than_50(capsys, app):
    with mock.patch('builtins.input', lambda x: 49):
        app()
        captured = capsys.readouterr()
        price = 4000
        "Your wedding will cost "+str(price)+" dollars\n" == captured.out

@pytest.mark.it("More than 200 should be priced 20,000")
def test_t(capsys, app):
    with mock.patch('builtins.input', lambda x: 201):
        app()
        captured = capsys.readouterr()
        price = 20000
        "Your wedding will cost "+str(price)+" dollars\n" == captured.out



