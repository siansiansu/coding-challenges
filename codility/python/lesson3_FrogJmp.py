# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    jumps = Y - X
    if jumps % D == 0:
        return jumps // D
    else:
        return jumps // D + 1