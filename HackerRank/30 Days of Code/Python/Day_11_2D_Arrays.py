#!/bin/python3

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    max_total = -9 * 7
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            total = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i +
                                                                    1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            max_total = max(max_total, total)
    return max_total


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_total = hourglassSum(arr)
    print(max_total)
