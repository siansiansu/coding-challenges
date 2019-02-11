# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    if sorted(A) == [i for i in range(1, len(A) + 1)]:
        return 1
    else:
        return 0