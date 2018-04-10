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


def solution(N):
    max_gap = 0
    current_gap = 0

    # Skip the tailing zero(s)
    while N > 0 and N % 2 == 0:
        N //= 2

    while N > 0:
        remainder = N % 2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        N //= 2

    return max_gap


def solution(N):
  # write your code in Python 2.7

    s = str(bin(N)).strip("0b")

    sl = len(s)
    bg = 0
    temp = 0
    for i in range(sl):

        if s[i] == "0":
            bg += 1
        if s[i] == "1":
            if temp < bg:
                temp = bg
            bg = 0
    return temp
