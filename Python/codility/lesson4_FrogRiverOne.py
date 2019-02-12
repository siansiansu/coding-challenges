# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    S = set()
    count = len(A)
    for i in range(0, count):
        S.add(A[i])
        if(len(S) == X):
            return i
    return -1