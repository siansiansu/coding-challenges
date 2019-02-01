# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
    return min_dif