#!/usr/bin/python3
def safe_print_list_integers(my_list, x):
    i = 0
    j = 0
    if (x == 0):
        return(0)
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            j = j +1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return (j)
