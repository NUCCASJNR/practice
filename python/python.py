#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(num1 + 1, 10):
        print("{}{}".format(num1, num2))
    else:
        print("{}{}".format(num1, num2), end=", ")
