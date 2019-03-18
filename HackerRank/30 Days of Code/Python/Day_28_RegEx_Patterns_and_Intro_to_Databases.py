#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    names = []
    for N_itr in range(N):
        firstName, emailID = input().strip().split(' ')
        if '@gmail.com' in emailID:
            names.append(firstName)
    print(*sorted(names), sep='\n')
