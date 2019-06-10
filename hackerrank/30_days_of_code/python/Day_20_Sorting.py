#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here


def bubble_sort(collection):
    count = 0
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j +
                                          1] = collection[j + 1], collection[j]
                count += 1
        if not swapped:
            break
    return count, collection


count, collection = bubble_sort(a)
print("Array is sorted in {} swaps.".format(count))
print("First Element: {}".format(collection[0]))
print("Last Element: {}".format(collection[-1]))
