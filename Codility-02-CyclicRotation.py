# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    A2 = A[:]
    for i in range(len(A2)):
         A[(i + K) % len(A)] = A2[i]
    return A