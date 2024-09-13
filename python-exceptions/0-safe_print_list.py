#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # This will count how many items we actually print
    try:
        for i in range(x):  # We loop through the list and try to print 'x' items
            print(my_list[i], end="")  # Print each item without a new line
            count += 1  # Increase the count for each printed item
    except IndexError:  # This catches when we try to print more than the list has
        pass  # Do nothing, just stop trying to print more
    print()  # After printing all the items, print a new line
    return count  # Return how many items we actually printed
