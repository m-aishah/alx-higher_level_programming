#!/usr/bin/python3
for alphabet in range(122,96,-1):
    if alphabet % 2 == 0:
        diff = 0
    else:
        diff = 32
    print("{:c}" .format(alphabet - diff), end="")
