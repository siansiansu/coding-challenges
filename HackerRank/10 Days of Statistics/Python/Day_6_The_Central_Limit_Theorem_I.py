# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

x = 9800
mu = 49 * 205
sigma = math.sqrt(49) * 15


def cdf(x, mu, sigma): return 0.5 * \
    (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


print("%.4f" % (cdf(x, mu, sigma)))
