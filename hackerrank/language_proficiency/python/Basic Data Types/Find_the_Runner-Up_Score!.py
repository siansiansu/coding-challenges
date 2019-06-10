if __name__ == '__main__':
    n = int(input())
    arr = [i for i in map(int, input().split())]

    res = []
    for each in arr:
        if each != max(arr):
            res.append(each)
    print(max(res))
