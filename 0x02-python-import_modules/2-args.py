#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    number_of_arguments = len(argv) - 1
    argument = "argument"
    # make argument plural if the number of arguments is not 1
    if number_of_arguments != 1:
        argument += "s"

    if number_of_arguments == 0:
        print("{} {}.".format(number_of_arguments, argument))
    else:
        print("{} {}:".format(number_of_arguments, argument))

    for index in range(1, len(argv)):
        print("{}: {}".format(index, argv[index]))
