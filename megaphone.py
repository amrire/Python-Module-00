#!/usr/bin/python3
import sys

def megaphone():
    """Prints the arguments passed to the script in uppercase."""
    if len(sys.argv) < 2:
        print("* LOUD AND UNBEARABLE FEEDBACK NOISE *")
    else:
        for i in range(1, len(sys.argv)):
            print(sys.argv[i].upper(), end="")
        print()
        
if __name__ == "__main__":
    megaphone()
