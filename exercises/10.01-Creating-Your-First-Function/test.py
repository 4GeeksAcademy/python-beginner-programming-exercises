import io, sys, mock, pytest, os, re
sys.stdout = buffer = io.StringIO()

import app

@pytest.mark.it('The function add_numbers should exist and receive two params: a and b')
def test_function_exists():
    try:
        from app import add_numbers
    except ImportError:
        raise ImportError("The function 'add_numbers' should exist on app.py")

@pytest.mark.it('Use the function print()')
def test_for_print():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(.+\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("We tested the function add_numbers with 4 and 6 and it should return 10")
def test_call_sample():
    from app import add_numbers
    result = add_numbers(4,6)
    assert result == 10


@pytest.mark.it("We tested the function add_numbers with 13 and 6 and it should return 19")
def test_call_sample2():
    from app import add_numbers
    result = add_numbers(13,6)
    assert result == 19

@pytest.mark.it("Add the return statement inside the existing function")
def test_use_my_var1():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = r"return\s+.+"
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True

#     assert re.match(regex, content)
@pytest.mark.it('Console should output 7')
def test_add_variables(capsys):
    captured = buffer.getvalue()
    assert captured == str(7)+"\n"
