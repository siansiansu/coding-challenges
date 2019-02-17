#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    inp1 = Counter(a)
    inp2 = Counter(b)
    char_list = list(set(a + b))

    count = 0
    for each in char_list:
        count += abs(inp1[each] - inp2[each])
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
