#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
if number > 0:
    ln = number % 10
    if ln > 5:
        print(f"{string} {number} is {ln} and is greater 5")
    elif ln == 0:
        print(f"{string} {number} is {ln} and is 0")
    else:
        print(f"{string} {number} is {ln} and is less than 6 and not 0")
elif number == 0:
    ln = 0
    print(f"{string} {number} is {ln} and is 0")
else:
    ln = -number % 10
    ln = -ln
    if ln > 5:
        print(f"{string} {number} is {ln} and is greater 5")
    elif ln == 0:
        print(f"{string} {number} is {ln} and is 0")
    else:
        print(f"{string} {number} is {ln} and is less than 6 and not 0")