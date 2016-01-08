"""Lottery Picker

This program picks 6 numbers at random.
"""

import sys
import random
import re


def main():
    print("************ Lottery Picker ********************")
    print("Picks 6 numbers at random for you. It bases its randomisation on the")
    print(" python random algorithm and stats from previous draws")

    numberOfLuckyDips=input("How many sets of numbers do you want ?: ")

    for i in range(0, int(numberOfLuckyDips)):
        print(simple_rand_num_gen())


def simple_rand_num_gen():
    myWinningNumbers  = set([])
    while len(myWinningNumbers) < 6:
        myWinningNumbers.add(random.randint(1,59))

    return sorted(myWinningNumbers)

if __name__ == "__main__":
    main()