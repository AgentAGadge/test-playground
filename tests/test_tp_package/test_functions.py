import pytest
from tp_package.functions import add_one


# --- build_api_url - Unit Tests ---
# Refer to https://www.vcalc.com/wiki/vCalc/Haversine+-+Distance to check computations
@pytest.mark.parametrize("input, expected", [
    (0,1),
])
def test_add_one(input,expected):
  # Arrange
  # Act
  result = add_one(input)
  # Assert
  assert(expected==result)