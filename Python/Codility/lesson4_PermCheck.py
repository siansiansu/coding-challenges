# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6

    total = [i for i in range(1, len(A) + 1)]

    if sorted(A) == total:
        return 1
    else:
        return 0
