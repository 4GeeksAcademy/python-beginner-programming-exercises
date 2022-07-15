import io, sys, os, re, pytest
sys.stdout = buffer = io.StringIO()
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
import app

@pytest.mark.it("Create a variable named my_var1")
def test_my_var1_exists():
    try:
        from app import my_var1
    except ImportError:
        raise ImportError("The variable 'my_var1' should exist on app.py")

    
@pytest.mark.it("Create a variable named my_var2")
def test_my_var2_exists():
    try:
        from app import my_var2
    except ImportError:
        raise ImportError("The variable 'my_var2' should exist on app.py")

@pytest.mark.it("Variable my_var1 value should be 'Hello'")
def test_my_var1_value():
    from app import my_var1
    assert my_var1 == "Hello"

@pytest.mark.it("Variable my_var2 value should be 'World'")
def test_my_var1_value():
    from app import my_var2
    assert my_var2 == "World"
@pytest.mark.it("Variable my_var2 value should be 'World'")
def test_the_new_string_exists():
    import app
    try:
        app.the_new_string
    except AttributeError:
        raise AttributeError('The variable "the_new_string" should exist on app.py')

@pytest.mark.it('Print "Hello World" on the console')
def test_for_file_output():
    captured = buffer.getvalue()
    assert captured == "Hello World\n" #add \n because the console jumps the line on every print
def test_for_print_variable():
    
    with open(path, 'r') as content_file:
        content = content_file.read()
        # makes sure we are calling print function with a variable and not the hard coded string
        regex = re.compile(r"print\s*\(\s*[^\d\W][_a-zA-Z0-9]*\s*\)\s*")
        assert bool(regex.search(content)) == True