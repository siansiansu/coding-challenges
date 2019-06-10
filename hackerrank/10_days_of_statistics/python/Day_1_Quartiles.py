# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
arr = sorted(map(int, input().split()))
mid = len(arr) // 2


def median(arr):
    middle = len(arr) // 2
    if (len(arr) % 2 == 0):
        return (arr[middle - 1] + arr[middle]) / 2
    else:
        return arr[middle]


if (len(arr) % 2 == 0):
    Q1 = median(arr[:mid])
    Q3 = median(arr[mid:])
else:
    Q1 = median(arr[:mid])
    Q3 = median(arr[mid + 1:])

print(int(Q1))
print(int(median(arr)))
print(int(Q3))
