import pytest
import app

@pytest.mark.it('Function should be called with the sum of 3 + 4')
def test_for_return():
    from app import addNumbers
    result = addNumbers(3,4)
    assert result == 7

