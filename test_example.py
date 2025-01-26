"""
Basic Testing
"""

def test_addition():
    """
    Add Test
    """
    # Test if the addition of two numbers is correct
    result = 1 + 1
    assert result == 2, f"Expected 2, but got {result}"

def test_subtraction():
    """
    Sub Test
    """
    # Test if the subtraction of two numbers is correct
    result = 5 - 3
    assert result == 2, f"Expected 2, but got {result}"

def test_multiplication():
    """
    Mult Test
    """
    # Test if the multiplication of two numbers is correct
    result = 3 * 4
    assert result == 12, f"Expected 12, but got {result}"

def test_division():
    """
    Div Test
    """
    # Test if the division of two numbers is correct
    result = 10 / 2
    assert result == 5, f"Expected 5, but got {result}"
