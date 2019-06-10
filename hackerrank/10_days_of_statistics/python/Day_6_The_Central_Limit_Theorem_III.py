# Enter your code here. Read input from STDIN. Print output to STDOUT

samples = 100
mu = 500
sigma = 80
interval = 0.95
z = 1.96

sd_sample = sigma / (samples ** 0.5)

print('%.2f' % (mu - sd_sample * z))
print('%.2f' % (mu + sd_sample * z))
