#!/usr/bin/python3
"""Write a class MyList that inherits from list:"""


class MyList(list):
    """A class that inherits from list with an additional sorting display method."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original."""
 
        print(sorted(self))
