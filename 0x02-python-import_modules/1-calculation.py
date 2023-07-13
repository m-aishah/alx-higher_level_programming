#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    """Does some math using functions in calculator_1.py
    
    add - Adds 2 integers
    sub - Subtracts 2 integers
    mul - Multiplies 2 integers
    div - Divides 2 integers
    """
    a = 10
    b = 5

    print('{:d} + {:d} = {:d}' .format(a, b, add(a, b)))
    print('{:d} - {:d} = {:d}' .format(a, b, sub(a, b)))
    print('{:d} * {:d} = {:d}' .format(a, b, mul(a, b)))
    print('{:d} / {:d} = {:d}' .format(a, b, div(a, b)))
