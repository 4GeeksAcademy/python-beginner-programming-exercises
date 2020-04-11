import io, sys, os, re, pytest
sys.stdout = buffer = io.StringIO()
import app

@pytest.mark.it('Use the function print()')
def test_for_print():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(.+\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Create a variable named html_document")
def test_html_document_exists():
    try:
        from app import html_document
    except ImportError:
        raise ImportError("The variable 'html_document' should exist on app.py")

@pytest.mark.it('Concatenate all the variables together (in the right order) to set the value of html_document')
def test_for_concat():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        _regex = r"html_document(\s*)=(\s*)e(\s*)\+(\s*)c(\s*)\+(\s*)g(\s*)\+(\s*)a(\s*)\+(\s*)f(\s*)\+(\s*)h(\s*)\+(\s*)d(\s*)\+(\s*)b"
        regex = re.compile(_regex)
        assert bool(regex.search(content)) == True


@pytest.mark.it('Print a basic html layout on the console like this: <html><head><title></title></head><body></body></html>')
def test_for_file_output():
    captured = buffer.getvalue()
    assert captured == "<html><head><title></title></head><body></body></html>\n" #add \n because the console jumps the line on every print