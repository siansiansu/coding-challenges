if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        s = input().split()
        command = s[0]
        args = s[1:]
        if command != "print":
            eval('arr.{0}{1}'.format(command, tuple(map(int, args))))
        else:
            print(arr)
