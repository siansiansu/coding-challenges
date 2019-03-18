# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
X = list(map(float, input().strip().split()))
Y = list(map(float, input().strip().split()))

mu_x = sum(X) / N
mu_y = sum(Y) / N

sigma_x = (sum([(i - mu_x) ** 2 for i in X]) / N) ** 0.5
sigma_y = (sum([(i - mu_y) ** 2 for i in Y]) / N) ** 0.5

covariance = sum([(X[i] - mu_x) * (Y[i] - mu_y) for i in range(N)])
correlation_coefficient = covariance / (N * sigma_x * sigma_y)

print('%.3f' % correlation_coefficient)
