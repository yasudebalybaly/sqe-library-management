import pytest
from src.gradebook import validate_name


@pytest.mark.parametrize("name", [
    "Muhammad Yasir",
    "Ali Khan",
    "Ahmed-Ali",
])
def test_validate_name_valid(name):
    assert validate_name(name) is True


@pytest.mark.parametrize("name", [
    "",
    "A" * 51,
    "Yasir123",
    "Yasir@Khan",
])
def test_validate_name_invalid(name):
    with pytest.raises(ValueError):
        validate_name(name)

@pytest.mark.parametrize("name_length,expected_valid", [
    (0, False),
    (1, True),
    (49, True),
    (50, True),
    (51, False),
])
def test_validate_name_length_boundaries(name_length, expected_valid):
    name = "A" * name_length

    if expected_valid:
        assert validate_name(name) is True
    else:
        with pytest.raises(ValueError):
            validate_name(name)