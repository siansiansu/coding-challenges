#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    new_arr = [i - 1 for i in arr]        # 將 arr 調整成從 0 起始。
    swap = i = 0
    while i < len(new_arr):
        if new_arr[i] == (i):  # 如果該數字位置正確，則不用 swap。
            i += 1
            continue
        # 將數字交換到正確的位置。
        new_arr[new_arr[i]], new_arr[i] = new_arr[i], new_arr[new_arr[i]]
        swap += 1   # 計算交換的次數。
    return swap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
