#!/usr/bin/python3
for character in range(97, 123):
    if character != 113 and character != 101:
        print("{:c}".format(character), end="", )
