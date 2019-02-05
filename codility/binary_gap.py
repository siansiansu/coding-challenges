# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # write your code in Python 3.6
    _list = bin(N)[2:]

    cnt = 0
    ans = 0
    for i in _list:
        if i == '0':
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    return ans

def solution2(N):
    return len(max(format(N, "b").strip("0").split("1")))