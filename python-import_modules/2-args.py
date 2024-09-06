#!/usr/bin/python3
import sys

def main():
    """
    Prints the number of arguments and the list of arguments
    passed to the script from the command line.
    """
    # Check the number of arguments passed (including the script name)
    num_args = len(sys.argv)

    # Case when no additional arguments are passed
    if num_args == 1:
        print("0 arguments.")
    # Case when exactly one argument (excluding the script name) is passed
    elif num_args == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    # Case when more than one argument is passed
    else:
        print(f"{num_args - 1} arguments:")
        # Iterate through each argument and print its index and value
        for i in range(1, num_args):
            print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    main()
