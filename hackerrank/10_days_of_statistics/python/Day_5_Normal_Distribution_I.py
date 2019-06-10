# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
mean, std = 20, 2


def cdf(x): return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))
