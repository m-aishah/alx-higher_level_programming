#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    no_of_rows = len(matrix[:])
    no_of_columns = len(matrix[0][:])

    for i in range(no_of_rows):
        for integer in matrix[i]:
            print("{:d}".format(integer), end=" ")
        print()
