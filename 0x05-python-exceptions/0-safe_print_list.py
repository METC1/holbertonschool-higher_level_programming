#!/usr/bin/python3
def safe_print_list(my_list, x):
    i = 0
    if (x == 0):
        print("")
        return(0)
    for i in range(0, x):
        try:
            print(my_list[i], end="")
        except IndexError:
            i = i - 1
            break
    print("")
    return (i+1)
