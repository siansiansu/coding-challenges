# Enter your code here. Read input from STDIN. Print output to STDOUT

nums = list(map(int, input().split()))

p = nums[0] / nums[1]

n = int(input())

print(round(sum(p * pow((1-p), (x-1)) for x in range(1, n+1)), 3))
