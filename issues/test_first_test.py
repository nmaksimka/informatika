import pytest


@pytest.mark.parametrize("input_a, input_b, expected_output", [
    (1, 1, 2),
    (2, 2, 4),
    (3, 5, 8),
])
def test_addition(input_a, input_b, expected_output):
    assert input_a + input_b == expected_output
