#!/usr/bin/python3

"""An empty class that defines a square"""


class Square:
    """Creating the class"""

    def __init__(self, size=0):
        """initializing the square class
        Args:
            size(int): size of the square
        Raises:
            TypeError: if size is not  an integer
            ValueError: if size is < 0

        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
            """Returns the area of the square"""

            return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""

        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """ prints in stdout the square with the character #
        print an empty line if size = 0"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)