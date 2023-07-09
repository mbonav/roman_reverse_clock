import numpy as np


# Task 1: Convert Roman numeral to integer
def roman_to_integer(roman_numeral):
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    subtractive_groups = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    # Convert the Roman numeral to uppercase for consistent handling
    roman_numeral = roman_numeral.upper()

    try:
        result = 0
        i = 0
        while i < len(roman_numeral):
            # Check for subtractive group
            if (
                i < len(roman_numeral) - 1
                and roman_numeral[i : i + 2] in subtractive_groups
            ):
                subtractive_value = subtractive_groups[roman_numeral[i : i + 2]]
                result += subtractive_value
                i += 2  # Skip the subtractive group
            else:
                result += roman_values[roman_numeral[i]]
                i += 1

        # Check for invalid subtractive group
        for group in subtractive_groups.keys():
            if group in roman_numeral:
                idx = roman_numeral.index(group)
                if idx < len(roman_numeral) - len(group):
                    next_value = roman_values[roman_numeral[idx + len(group)]]
                    group_value = subtractive_groups[group]
                    if next_value >= group_value:
                        return None, "Invalid Roman numeral: Invalid subtractive group"

        return result
    except KeyError as e:
        invalid_character = e.args[0]
        return None, f"Invalid Roman numeral: Unknown character '{invalid_character}'"
    except ValueError as e:
        return None, str(e)


# Task 2: Reverse words in a string
def reverse_words(string):
    # Split the string into an array of words
    words = np.array(string.split())

    # Reverse each word using array slicing
    reversed_words = np.array([word[::-1] for word in words])

    # Join the reversed words back into a string
    reversed_string = " ".join(reversed_words)

    return reversed_string


# Task 3: Calculate the angle between clock hands


def angle_between_hands(hours, minutes):
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        result = None
        return result, "Invalid time: Time values are out of range"

    try:
        hour_angle = 0.5 * (hours % 12 * 60 + minutes)
        minute_angle = 6 * minutes

        angle = np.abs(hour_angle - minute_angle)
        angle = np.min([angle, 360 - angle])

        result = angle.item()

        return result
    except ValueError as e:
        return result, str(e)
