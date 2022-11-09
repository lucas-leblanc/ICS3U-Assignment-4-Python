# Copyright (c) 2022 Lucas LeBlanc All rights reserved.
#
# Created by: Lucas LeBlanc
# Created on: Nov 2022
# ICS3U-Assignment-4-Python,
# This program tells you what day of the week it is


def main():

    # input and variables
    input_number_as_string = input("Enter week day number 1-7: ")

    # process and output
    try:
        input_number_as_int = int(input_number_as_string)
        if input_number_as_int == 1:
            print("\nThe {0:,}st day of the week is Sunday.".format(input_number_as_int))
        elif input_number_as_int == 2:
            print("\nThe {0:,}nd day of the week is Monday.".format(input_number_as_int))
        elif input_number_as_int == 3:
            print("\nThe {0:,}rd day of the week is Tuesday.".format(input_number_as_int))
        elif input_number_as_int == 4:
            print("\nThe {0:,}th day of the week is Wednesday.".format(input_number_as_int))
        elif input_number_as_int == 5:
            print("\nThe {0:,}th day of the week is Thursday.".format(input_number_as_int))
        elif input_number_as_int == 6:
            print("\nThe {0:,}th day of the week is Friday.".format(input_number_as_int))
        elif input_number_as_int == 7:
            print("\nThe {0:,}th day of the week is Saturday.".format(input_number_as_int))
        else:
            print("\n {} is not a number in the week.".format(input_number_as_int))
    except ValueError:
        print("\nThis is not a number of the week")

    print("\n\nDone.")

if __name__ == "__main__":
    main()
