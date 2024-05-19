def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()  # Print a new line after printing all integers
    except IndexError:
        pass
    finally:
        return count
