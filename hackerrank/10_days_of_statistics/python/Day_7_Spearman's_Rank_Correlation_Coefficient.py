# Enter your code here. Read input from STDIN. Print output to STDOUT


def get_rank(X, n):
    x_rank = dict((x, i + 1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rank_x = get_rank(X, n)
rank_y = get_rank(Y, n)

d = [(rank_x[i] - rank_y[i]) ** 2 for i in range(n)]

rxy = 1 - (6 * sum(d)) / (n * (n ** 2 - 1))

print('%.3f' % rxy)
