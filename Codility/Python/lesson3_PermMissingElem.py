# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    start = 1
    end = len(A) + 1
    total = ((start + end) * (N + 1)) / 2
    return int(total - sum(A))