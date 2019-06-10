# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = sorted(map(int, input().split()))

mean = sum(arr) / n
variance = sum([((each - mean) ** 2) for each in arr]) / n
stddev = variance ** 0.5

print("{0:0.1f}".format(stddev))
