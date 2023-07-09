from code import *


def test_code():
    if __name__ == "__main__":
        # Task 1: Roman numeral to integer
        roman_numeral = "MCMXC"
        value = roman_to_integer(roman_numeral)
        print(f"Roman numeral: {roman_numeral}")
        print(f"Integer value: {value}")

        # Task 2: Reverse words in a string
        string = "Hello World! OpenAI is awesome."
        reversed_string = reverse_words(string)
        print(f"Original string: {string}")
        print(f"Reversed string: {reversed_string}")

        # Task 3: Angle between clock hands
        hours = 10
        minutes = 30
        angle = angle_between_hands(hours, minutes)
        print(f"Time: {hours:02d}:{minutes:02d}")
        print(f"Angle between hands: {angle} degrees")
