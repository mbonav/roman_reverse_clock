import numpy as np

# Task 1: Convert Roman numeral to integer
def roman_to_integer(roman_numeral):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Convert Roman numeral characters to decimal values 
    values = np.array([roman_values[char] for char in roman_numeral])

    # Calculate the result by summing the decimal values while accounting for subtractive notation
    result = np.sum(np.where(values[:-1] < values[1:], -values[:-1], values[:-1])) + values[-1]

    return result

# Task 2: Reverse words in a string
def reverse_words(string):
    # Split the string into an array of words 
    words = np.array(string.split())

    # Reverse each word using array slicing
    reversed_words = np.array([word[::-1] for word in words])

    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string


# Task 3: Calculate the angle between clock hands
def angle_between_hands(hours, minutes):
    # Calculate the hour angle and minute angle 

    if hours >= 12:
        hours -= 12
        
    hour_angle = 0.5 * (60 * hours + minutes)
    minute_angle = 6 * minutes

    # Compute the absolute difference between the angles 
    angle = np.abs(hour_angle - minute_angle)

    # Determine the minimum angle by comparing the angle with its complement (360 - angle)
    angle = np.minimum(angle, 360 - angle)

    return angle 