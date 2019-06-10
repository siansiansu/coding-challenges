# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
data = sorted([int(i) for i in input().split()])

mean = sum(data)/n
median = (data[n // 2] + data[-(n//2 + 1)]) / 2
mode = sorted(sorted(Counter(data).items()),
              key=lambda x: x[1], reverse=True)[0][0]

print(mean)
print(median)
print(mode)
