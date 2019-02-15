#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    moves = 0
    q = [P-1 for P in q]
    for i, P in enumerate(q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1, 0), i):
            if q[j] > P:
                moves += 1
    print(moves)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
