#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):

    n_swap = 0
    for i in range(len(a)-1):

        for j in range(len(a)-1-i):

            if a[j] > a[j+1]:

                a[j+1], a[j] = a[j], a[j+1]
                n_swap +=1

    print ("Array is sorted in %d swaps." % n_swap)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
