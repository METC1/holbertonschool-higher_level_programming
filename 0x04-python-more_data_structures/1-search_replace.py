#!/usr/bin/python3


def search_replace(my_list, search, replace):
    list2 = []
    for i in my_list:
        if i == search:
            list2 += [replace]
        else:
            list2 += [i]
    return list2
