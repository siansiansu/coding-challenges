# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    result = 0
    count = 0
    for i in A:
        if i == 0:
            count += 1
        elif i == 1:
            result += count

    if result > 1000000000:   # 車輛數若超過 1000000000，則返回 -1。
        return -1
    return result
