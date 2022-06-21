#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMatch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING word
#  2. STRING guesses
#

def findMatch(word, guesses):
    greens = {}
    yellows = {}
    for guess in guesses:
        green = 0
        yellow = 0
        for i in range(5):
            if guess[i] == word[i]:
                greens += 1
            elif guess[i] in word:
                yellows += 1
        greens[guess] = green
        yellows[guess] = yellow
    print(greens, yellows)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    word = input()

    guesses = input()

    result = findMatch(word, guesses)

    fptr.write(result + '\n')

    fptr.close()
