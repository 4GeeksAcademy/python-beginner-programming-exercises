import io, mock, pytest, os, re, sys

@pytest.mark.it('You should create a function named add_numbers')
def test_function_exists(app):
    try:
        app.add_numbers
    except AttributeError:
        raise AttributeError("The function 'add_numbers' should exist on app.py")

@pytest.mark.it('The function add_numbers should return 15 when trying with 7 and 8')
def test_7_plus_8(app):
    try:
        assert app.add_numbers(7, 8) == 15
    except AttributeError:
        raise AttributeError("The function 'add_numbers' should exist")

@pytest.mark.it('The function add_numbers should return 50 when trying with 15 and 35')
def test_15_plus_35(app):
    try:
        assert app.add_numbers(15, 35) == 50
    except AttributeError:
        raise AttributeError("The function 'add_numbers' should exist")