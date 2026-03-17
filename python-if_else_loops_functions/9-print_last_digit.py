#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        ln = number % 10
        print(ln, end = "")
        return ln
    else:
        ln = -number % 10
        print(ln, end = "")
        return ln
