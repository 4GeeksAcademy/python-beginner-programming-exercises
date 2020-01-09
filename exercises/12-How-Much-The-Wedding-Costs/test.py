# from app import my_function
import pytest,os,re,io,sys, mock, json

@pytest.mark.it("Between 101 and 199")
def test__between_100_and_200(stdin):
    _input = json.loads(stdin)
    with mock.patch('builtins.input', lambda x: 199):
        sys.stdout = buffer = io.StringIO()
        import app
        price = 15000
        assert "Your wedding will cost "+str(price)+" dollars\n" == buffer.getvalue()

@pytest.mark.it("Between 100 and 51 should be 10,000")
def test_between_101_and_51(stdin):
    _input = json.loads(stdin)
    with mock.patch('builtins.input', lambda x: 100):
        sys.stdout = buffer = io.StringIO()
        import app
        price = 10000
        assert "Your wedding will cost "+str(price)+" dollars\n" == buffer.getvalue()


@pytest.mark.it("Less than 50 should be 4,000")
def test_less_than_50(stdin):
    _input = json.loads(stdin)
    with mock.patch('builtins.input', lambda x: 49):
        sys.stdout = buffer = io.StringIO()
        import app
        price = 4000
        "Your wedding will cost "+str(price)+" dollars\n" == buffer.getvalue()

@pytest.mark.it("More than 200 should be 20,000")
def test_t(stdin):
    _input = json.loads(stdin)
    with mock.patch('builtins.input', lambda x: 201):
        sys.stdout = buffer = io.StringIO()
        import app
        price = 20000
        "Your wedding will cost "+str(price)+" dollars\n" == buffer.getvalue()



