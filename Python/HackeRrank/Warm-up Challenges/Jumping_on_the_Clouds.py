#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    current = 0
    end = n - 1
    jumps = 0
    while current < end:
        # 如果下兩個位置為 0 的話，一次跳兩格
        if ((current + 2) <= end) and (c[current + 2] == 0):
            current += 2
            jumps += 1
        elif c[current + 1] == 0:        # 如果下一個位置為 0 的話，一次跳一格
            current += 1
            jumps += 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
