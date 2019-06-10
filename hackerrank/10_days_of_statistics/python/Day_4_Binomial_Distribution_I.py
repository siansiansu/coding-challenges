# Enter your code here. Read input from STDIN. Print output to STDOUT


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1 - p, n - k)


b, g = map(float, input().strip().split(' '))

result = round(sum([binomial(6, i, b / (b + g)) for i in range(3, 6+1)]), 3)
print(result)
