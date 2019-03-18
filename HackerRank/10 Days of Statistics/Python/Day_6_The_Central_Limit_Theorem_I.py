# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

x = 9800
mu = 49 * 205
sigma = math.sqrt(49) * 15


def normal_distro_cdf(x, mu, sigma):
    return "%.4f" % (1/2 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2)))))


print(normal_distro_cdf(x, mu, sigma))
