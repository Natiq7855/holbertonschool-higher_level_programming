#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    number = 0
    for i in range(len(roman_string)):
        current_val = rom_dict.get(roman_string[i], 0)
        if i + 1 < len(roman_string):
            next_val = rom_dict.get(roman_string[i + 1], 0)
            if current_val < next_val:
                number -= current_val
            else:
                number += current_val
        else:
            number += current_val
    return number
