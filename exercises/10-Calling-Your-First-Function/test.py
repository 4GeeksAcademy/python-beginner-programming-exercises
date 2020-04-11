import io, mock, pytest, os, re, sys

@pytest.mark.it('Use the function print()')
def test_for_print():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(.+\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Call the is_odd function and pass the value 45345")
def test_call_is_odd():
    with mock.patch('app.is_odd') as mocked_is_odd:
        from app import my_main_code
        my_main_code()
        mocked_is_odd.assert_called_with(45345)

@pytest.mark.it('The console should output "True" inside the function my_main_code ')
def test_for_file_output(capsys):
    from app import my_main_code
    my_main_code()
    captured = capsys.readouterr()
    assert captured.out == "True\n"
