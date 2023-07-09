import pytest
from code import roman_to_integer, reverse_words, angle_between_hands


# Test cases for roman_to_integer function
@pytest.mark.parametrize(
    "roman_numeral, expected_value",
    [
        ("I", 1),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MCMXC", 1990),
        ("MMVIII", 2008),
        ("MDCLXVI", 1666),
    ],
)
def test_roman_to_integer(roman_numeral, expected_value):
    assert roman_to_integer(roman_numeral) == expected_value


# Test cases for reverse_words function
@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Hello World!", "olleH dlroW!"),
        ("OpenAI is awesome.", "IAnepO si emosewa."),
        ("This is a test", "sihT si a tset"),
        ("", ""),
        ("Single", "elgniS"),
    ],
)
def test_reverse_words(string, expected_result):
    assert reverse_words(string) == expected_result

# Test cases for angle_between_hands function
@pytest.mark.parametrize('hours, minutes, expected_angle', [
    (12, 0, 0),
    (3, 0, 90),
    (6, 30, 15),
    (9, 45, 22.5),
    (11, 59, 5.5),
])
def test_angle_between_hands(hours, minutes, expected_angle):
    assert angle_between_hands(hours, minutes) == pytest.approx(expected_angle, abs=0.01)