# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st

n = int(input())
element = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(len(element)):
    s += [element[i]] * freq[i]

s.sort()

n = len(s)
n2 = int(n / 2)

Q1 = st.median(s[:n2])
Q3 = st.median(s[-n2:])

print(round(float(Q3 - Q1), 1))
