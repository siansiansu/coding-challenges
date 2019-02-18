# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    ints = [0] * (N + 2)

    for num in A:
        if 1 <= num <= N:
            ints[num] += 1

    for ind in range(1, N + 2):
        if ints[ind] == 0:
            return ind
    return -1