# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    head = 0
    tail = sum(A)
    res = float('Inf')
    for ixn in A[:-1]:
        head += ixn
        tail -= ixn
        res = min(res, abs(head - tail))
    return res