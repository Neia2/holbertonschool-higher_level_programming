#!/usr/bin/python3
import sys

def main():
    """Calculate and print the sum of command-line arguments."""
    total_sum = 0

    # Iterate over each argument
    for arg in sys.argv[1:]:
        try:
            # Convert argument to integer and add to total_sum
            total_sum += int(arg)
        except ValueError:
            # Handle the case where conversion fails
            print("Error: All arguments must be integers.")
            return

    # Print the total sum of all arguments
    print(total_sum)

if __name__ == "__main__":
    main()
