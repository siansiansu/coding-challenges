# Enter your code here. Read input from STDIN. Print output to STDOUT


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1 - p, n - k)


p, n = list(map(int, input().split(" ")))

print(round(sum([binomial(n, i, p/100) for i in range(3)]), 3))
print(round(sum([binomial(n, i, p/100) for i in range(2, n + 1)]), 3))
