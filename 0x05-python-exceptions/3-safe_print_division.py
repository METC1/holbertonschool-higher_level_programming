#!/usr/bin/python3
def safe_print_division(a, b):
    i = 0
    res = 0.0
        try:
            res = a / b
            i = 1
        except (ValueError, TypeError):
            pass
        finally:
            if i == 1:
                print("Inside result: {}".format(res))
                return res
            else:
                print("Inside result: {}".format("None"))
            
