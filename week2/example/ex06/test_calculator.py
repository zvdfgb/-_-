import pytest
from calculator import safe_divide

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (1, 3, 0.3333),
    (-8, 2, -4.0),
    (0, 5, 0.0),
])
def test_safe_divide_success(a, b, expected):
    assert safe_divide(a, b) == expected

def test_safe_divide_zero_exception():
    with pytest.raises(ValueError, match="Division by zero"):
        safe_divide(10, 0)
