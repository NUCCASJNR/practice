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

        #self.__size = size

