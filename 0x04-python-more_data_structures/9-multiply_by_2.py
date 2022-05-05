#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    dict2 = a_dictionary.copy()
    for i, num in dict2.items():
        dict2[i] = num * 2
    return dict2
