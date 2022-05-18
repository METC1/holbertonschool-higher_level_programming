#!/usr/bin/python3
def safe_print_list(my_list, x):
    for i in range(0, x):
        try:
            print(my_list[i], end="")
        except StandardError:
            i = i - 1
            break
    print("")
    return (i+1)