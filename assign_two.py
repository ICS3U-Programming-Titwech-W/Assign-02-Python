#!/usr/bin/env python3
# Created by: Titwech wal
# Created on: Mar. 29. 2022

# This program asks the user for a number
# To calculate the surafce area and
# Volume of a tetrahedron

import math
from colorama import Fore


def main():
    # get input from user for edge
    print("Lets calculate the area and")
    print("volume of a tetrahedron")
    print("")
    side = float(input(Fore.YELLOW + "Enter the side (cm): "))

    # calculate area and volume
    area = (math.sqrt(3) * (side * side))
    volume = ((math.pow(side, 3) / (6 * math.sqrt(2))))

    # display the results to the user
    print("")
    print(Fore.CYAN + "Area = {:.2f} cm". format(area))
    print("Volume = {:.2f} cm". format(volume))


if __name__ == "__main__":
    main()
