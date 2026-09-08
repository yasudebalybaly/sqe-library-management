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