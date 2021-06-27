from src.cli.cli import unique_characters
import pytest


@pytest.mark.parametrize('string, expected_result', [("checking", 6),
                                                     ("expected", 5),
                                                     ("output", 2)
                                                     ])
def test_unique_characters(string, expected_result):
    assert unique_characters(string) == expected_result


@pytest.mark.parametrize('string, expected_result', [(
    (10, 20, 30), "Invalid input, only strings expected!"),
    (True, "Invalid input, only strings expected!"),
])
def test_invalid_input(string, expected_result):
    # In the case of passing a tuple function and a boolean value.
    assert unique_characters(string) == expected_result
