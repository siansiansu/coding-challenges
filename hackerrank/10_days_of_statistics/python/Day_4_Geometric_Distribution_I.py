# Enter your code here. Read input from STDIN. Print output to STDOUT

nums = list(map(int, input().split()))

p = nums[0] / nums[1]

k = int(input())

print(round((pow((1-p), (k-1))) * p, 3))
