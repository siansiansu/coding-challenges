# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def is_prime(n):
    if n == 1:
        return "Not prime"

    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return "Not prime"
    return "Prime"


T = int(input())
for each in range(T):
    n = int(input())
    print(is_prime(n))
