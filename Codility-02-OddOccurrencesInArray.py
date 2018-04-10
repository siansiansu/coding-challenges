# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    import collections
    B = collections.Counter(A)

    for i in set(A):
        if B[i] == 1:
            return i


def solution(A):
    result = 0
    for number in A:
        result ^= number

    return result
