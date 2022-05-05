#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    ordered = sorted(a_dictionary.keys())
    for i in ordered:
        print("{:s}: {}".format(i, a_dictionary[i]))
