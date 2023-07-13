#!/usr/bin/python3
if __name__ == "__main__":
    from sys import exit, argv

    number_of_arguments = len(argv) - 1

    if number_of_arguments != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, operator, b = argv[1], argv[2], argv[3]
    if (operator == '+'):
        result = int(a) + int(b)
    elif (operator == '-'):
        result = int(a) - int(b)
    elif (operator == '*'):
        result = int(a) * int(b)
    elif (operator == '/'):
        result = int(a) / int(b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}" .format(a, operator, b, result))
    exit(0)

