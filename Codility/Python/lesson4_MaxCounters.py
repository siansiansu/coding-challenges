# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):
    # write your code in Python 3.6
    result = [0] * N
    minValue = 0
    maxValue = 0
    for number in A:
        index = number - 1
        if(index == N):
            minValue = maxValue
            continue
        result[index] = max(result[index], minValue) + 1
        maxValue = max(maxValue, result[index])
    for i in range(N):
        result[i] = max(result[i], minValue)
    return result
