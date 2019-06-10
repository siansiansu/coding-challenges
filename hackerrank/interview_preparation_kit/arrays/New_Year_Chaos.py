#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    moves = 0
    q = [i - 1 for i in q]

    for ix, ixn in enumerate(q):
        if ixn - ix > 2:    # 如果原來的位置 ixn - 後來的位置大於 2，則 return "Too chaotic"，因為一個人最多只能賄絡兩次。
            print("Too chaotic")
            return

        for j in range(max(ixn - 1, 0), ix):
            if q[j] > ixn:
                moves += 1
    print(moves)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
