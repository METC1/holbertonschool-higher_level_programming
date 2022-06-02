#!/usr/bin/python3
"""
    Class mylist inherits from list
    will contain method that prints sorted list
"""


class Mylist(list):
    """
    Class My_List inherits from list
    """

    def print_sorted(self):
        """
        Method to print the list sorted ascending
        """

        print(sorted(self))
