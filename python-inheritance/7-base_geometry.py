#!/usr/bin/python3
"""empty class"""


class BaseGeometry():
    """an empty class"""

    def area(self):
        """asd sd"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """asa ass"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
