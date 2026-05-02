#!/usr/bin/python3
"""Write a class MyList that inherits from list:"""


class MyList(list):
    """Aclassthatinheritsfromlistwithanadditionalsortingdisplaymethod."""

    def print_sorted(self):
        """Printsthelistinascendingorderwithoutmodifyingtheoriginal."""

        print(sorted(self))
