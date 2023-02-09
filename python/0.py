#!/usr/bin/python3
def print_list_integer(my_list=[]):
    tot = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            tot += 1
        except IndexError:
            break
    print()
    return tot
