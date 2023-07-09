import re


# Task 1: Convert Roman numeral to integer
def roman_to_integer(roman_numeral):
    #initialising the dictionary
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    prev_value = 0
    
    # loop trough the caracters in reverse order 
    # to retrieve the corresponding decimal value from the dictionary
    for char in roman_numeral[::-1]:
        value = roman_values[char]
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value

    return result

# Task 2: Reverse words in a string
def reverse_words(string):
    # Split the string into words using regular expression
    words = re.findall(r"\w+", string)

    # Reverse each word
    reversed_words = [word[::-1] for word in words]

    # Reconstruct the string with reversed words
    result = re.sub(r"\w+", lambda m: reversed_words.pop(0), string)

    return result


# Task 3: Calculate the angle between clock hands
def angle_between_hands(hours, minutes):
    # accounting for the 24-hour format
    if hours >= 12:
        hours -= 12
        
    # Calculate the angles for the hour and minute hands
    hour_angle = 0.5 * (60 * (hours % 12) + minutes)
    minute_angle = 6 * minutes

    # Calculate the absolute difference between the angles
    angle = abs(hour_angle - minute_angle)

    # Take the smaller angle between the two possible angles
    angle = min(angle, 360 - angle)

    return angle
