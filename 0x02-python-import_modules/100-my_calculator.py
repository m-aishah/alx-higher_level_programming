#!/usr/bin/python3
if __name__ == "__main__":
    from sys import exit, argv
    from calculator_1 import add, sub, mul, div

    number_of_arguments = len(argv) - 1

    if number_of_arguments != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, operator, b = int(argv[1]), argv[2], int(argv[3])
    if (operator == '+'):
        result = add(a, b)
    elif (operator == '-'):
        result = sub(a, b)
    elif (operator == '*'):
        result = mul(a, b)
    elif (operator == '/'):
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}" .format(a, operator, b, result))
    exit(0)
