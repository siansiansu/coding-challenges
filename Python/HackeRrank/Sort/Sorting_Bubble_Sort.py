#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.


def countSwaps(a):
    count = 0
    swapped = False

    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
                swapped = True
        if not swapped:
            break

    print('Array is sorted in', count, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
