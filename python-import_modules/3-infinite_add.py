#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    count = len(argv)
    result = 0
    if count == 0:
        print("0")
    for i in range(count):
        result = result + int(argv[i])
    print(result)
