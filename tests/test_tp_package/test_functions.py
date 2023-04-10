"""
This file contains unit tests for tp_package.functions.py
"""

import pytest
from tp_package.functions import add_one


@pytest.mark.parametrize("input_value, expected", [
    (0, 1),
])
def test_add_one(input_value, expected):
    """
    Test add_one
    """
    # Arrange
    # Act
    res = add_one(input_value)
    # Assert
    assert expected == res
