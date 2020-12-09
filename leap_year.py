#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program checks if it is a leap year or common year

import math


def main():
    # This function checks if it is a leap year or common year

    # Input

    chosen_year = input("Enter the year you have chosen: ")
    print("")

    # process
    try:
        if (int(chosen_year) % 4) == 0:
            if (int(chosen_year) % 100) == 0:
                if (int(chosen_year) % 400) == 0:
                    print("{} is a leap year".format(chosen_year))
                else:
                    print("{} is a common year".format(chosen_year))
            else:
                print("{} is a leap year".format(chosen_year))
        else:
            print("{} is a common year".format(chosen_year))
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
