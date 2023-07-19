#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman Numeral to an integer"""

    if (not isinstance(roman_string, str) or roman_string == 'None'):
        return 0
    roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    output = 0

    for index, character in enumerate(roman_string):
        if roman_numerals.get(character, 0) == 0:
            return 0

        if (index != (len(roman_string) - 1) and
                (roman_numerals[roman_string[index]] < roman_numerals[roman_string[index + 1]])):

                output += roman_numerals[character] * -1

        else:
            output += roman_numerals[character]

    return output
