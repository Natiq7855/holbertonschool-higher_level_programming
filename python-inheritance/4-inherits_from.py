#!/usr/bin/python3
"""check inherity"""


def inherits_from(obj, a_class):
    """fuction of it"""

    return isinstance(obj, a_class) and type(obj) is not a_class
