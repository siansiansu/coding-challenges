# Enter your code here. Read input from STDIN. Print output to STDOUT

mu_1, mu_2 = [float(num) for num in input().split(" ")]

cost_1 = 160 + 40 * (mu_1 + mu_1 ** 2)
cost_2 = 128 + 40 * (mu_2 + mu_2 ** 2)

print(round(cost_1, 3))
print(round(cost_2, 3))
