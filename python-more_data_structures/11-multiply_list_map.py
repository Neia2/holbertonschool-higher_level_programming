#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Use map() to multiply each item in the list by the given number
    return list(map(lambda x: x * number, my_list))

