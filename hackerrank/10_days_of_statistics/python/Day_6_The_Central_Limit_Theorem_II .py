# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

x = 250
mu = 2.4*100
sigma = 100**(1/2)*2.0


def cdf(x, mu, sigma): return 0.5 * \
    (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))


print('%.4f' % cdf(x, mu, sigma))
