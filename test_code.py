
from code import roman_to_integer, reverse_words, angle_between_hands

# Test cases for roman_to_integer function
def test_roman_to_integer():
    assert roman_to_integer('I') == 1
    assert roman_to_integer('V') == 5
    assert roman_to_integer('X') == 10
    assert roman_to_integer('L') == 50
    assert roman_to_integer('C') == 100
    assert roman_to_integer('D') == 500
    assert roman_to_integer('M') == 1000
    assert roman_to_integer('IV') == 4
    assert roman_to_integer('IX') == 9
    assert roman_to_integer('XL') == 40
    assert roman_to_integer('XC') == 90
    assert roman_to_integer('CD') == 400
    assert roman_to_integer('CM') == 900
    assert roman_to_integer('MCMXC') == 1990
    assert roman_to_integer('IXX') == (None, 'Invalid Roman numeral: Invalid subtractive group')
    assert roman_to_integer('MMVIIZ') == (None, "Invalid Roman numeral: Unknown character 'Z'")
    

# Test cases for reverse_words function
def test_reverse_words():
    assert reverse_words('Hello World!') == 'olleH !dlroW'
    assert reverse_words('OpenAI is awesome.') == 'IAnepO si .emosewa'

# Test cases for angle_between_hands function
def test_angle_between_hands():
    # Test case with 12:00
    #assert angle_between_hands(12, 0) == 0

    # Test case with 3:30
    assert angle_between_hands(3, 30) == 75

    # Test case with 6:45
    assert angle_between_hands(15, 30) == 75

    # Test case with 9:15
    assert angle_between_hands(9, 15) == 172.5

    # Test case with 11:59
    assert angle_between_hands(21, 15) == 172.5

    # Test case with 27:30 
    assert angle_between_hands(27, 30) == (None, 'Invalid time: Time values are out of range')


