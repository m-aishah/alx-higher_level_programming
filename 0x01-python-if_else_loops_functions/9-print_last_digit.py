#!/usr/bin/python3
def print_last_digit(number):
    if int(number) < 0:
        lastDigit = (number * -1) % 10
    else:
        lastDigit = number % 10
    print("{:d}" .format(lastDigit), end="")
    return lastDigit
