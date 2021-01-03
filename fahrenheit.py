#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on January 2021
# This program converts celsius into fahrenheit


def fahrenheit():
    # this function converts celsius into fahrenheit

    # input
    celsius_temp = input("Enter a temperature (°C): ")
    print("")

    # process
    try:
        celsius_temp_int = int(celsius_temp)

        fahrenheit_temp = (9/5) * celsius_temp_int + 32

        # output
        print("{0}°C is equal to {1}°F.".format(celsius_temp_int,
                                                fahrenheit_temp))
    except Exception:
        # output
        print("That's not a temperature! Try again.")


def main():
    # calls other functions

    # fahrenheit function
    fahrenheit()


if __name__ == "__main__":
    main()
