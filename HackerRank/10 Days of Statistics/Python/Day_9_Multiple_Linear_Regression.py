# Enter your code here. Read input from STDIN. Print output to STDOUT

from sklearn.linear_model import LinearRegression

B = LinearRegression()
m, n = map(int, input().split())
flat = [*map(float, [_ for list in [input().split()
                                    for _ in range(n)] for _ in list])]

X = [flat[i:i+m] for i in range(0, n*(m+1), m+1)]
Y = [flat[i] for i in range(m, n*(m+1), m+1)]

B.fit(X, Y)

q = int(input())

X = [[*map(float, input().split())] for _ in range(q)]
Y = B.predict(X)

print('\n'.join('%f' % y for y in Y))
