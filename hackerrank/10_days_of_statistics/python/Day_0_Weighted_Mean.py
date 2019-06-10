# Enter your code here. Read input from STDIN. Print output to STDOUT

N = map(int, input().split())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))

sum_X = sum([a * b for a, b in zip(X, W)])
print(round((sum_X/sum(W)), 1))
